import scrapy
from crawler.models import AmazonProduct


class AmazonSpider(scrapy.Spider):
    name = "amazonSpider"
    start_urls = ["https://www.amazon.in/gp/bestsellers/"]

    def start_requests(self):
        headers = {
            "cookie": "session-id=261-0423817-4284533; i18n-prefs=INR; ubid-acbin=260-9536726-4137347; csm-hit=tb:A66BGQMC56131P7KZ9YG+s-A66BGQMC56131P7KZ9YG|1661938038725&t:1661938038725&adb:adblk_yes; session-token=cjJGeI4cpAcgaeDeO1s0KCC/G7QgNmdopz0rJ36VnXSj0STq5jsO91q2WNtml5LSD5wDG9wcSlfvPhI6WODNbkLHB+6+SQuH5S9tmWavNapCmLU2AG3Hgiw1Wddq9cbv0dXRTFgyXEEo02ivmXUTNvs5PSNQTRVOhGdVy1Z6gjfmJhfxbY+WWNLeuCwfTU3DqW4pw+cZwUS97Q0CU2axkSVijOpXybC/; session-id-time=2082758401l",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        }
        for url in self.start_urls:  # Empty list by default
            url = url + f"{self.category.strip()}?pg=1"
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        items = {}
        current_page = response.url.split("pg=")[1]
        items[current_page] = []

        for _ in range(1, 51):
            product = response.xpath(
                f"/html/body/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div[{_}]"
            )
            if product:
                # Pass each product to parse_item
                item = self.parse_item(product)
                if item:
                    items[current_page].append(item)

        # Handle pagination
        next_page = response.css("ul.a-pagination li.a-last a::attr(href)").get()
        if next_page:
            headers = {
                "cookie": "session-id=261-0423817-4284533; i18n-prefs=INR; ubid-acbin=260-9536726-4137347; csm-hit=tb:A66BGQMC56131P7KZ9YG+s-A66BGQMC56131P7KZ9YG|1661938038725&t:1661938038725&adb:adblk_yes; session-token=cjJGeI4cpAcgaeDeO1s0KCC/G7QgNmdopz0rJ36VnXSj0STq5jsO91q2WNtml5LSD5wDG9wcSlfvPhI6WODNbkLHB+6+SQuH5S9tmWavNapCmLU2AG3Hgiw1Wddq9cbv0dXRTFgyXEEo02ivmXUTNvs5PSNQTRVOhGdVy1Z6gjfmJhfxbY+WWNLeuCwfTU3DqW4pw+cZwUS97Q0CU2axkSVijOpXybC/; session-id-time=2082758401l",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
            }
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(
                url=next_page_url, headers=headers, callback=self.parse
            )

        yield items

    def _rupee_to_float(self, price):
        if not price:
            return 0.0
        return float(price.replace("₹", "").replace(",", ""))

    def parse_item(self, product):
        """Parse individual product data"""
        # Create Selector object from the extracted HTML
        product_sel = scrapy.Selector(text=product.get())

        # Extract product details
        product_name = product_sel.xpath("//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'a-link-normal', ' ' ))]//span//div/text()").extract_first()
        product_price = product_sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_cDEzb_p13n-sc-price_3mJ9Z", " " ))]/text()').extract_first()
        product_image = product_sel.css('.p13n-product-image::attr(src)').extract_first()
        product_link = product_sel.css("a.a-link-normal::attr(href)").extract_first()

        if product_name:
            if self.save_to_db:
                AmazonProduct.objects.get_or_create(
                    name=product_name,
                    defaults={
                        "price": self._rupee_to_float(product_price),
                        "image_url": product_image or "",
                        "product_link": product_link or "",
                        "category": self.category,
                    }
                )
            
            return {
                product_name.strip(): {
                    "price": product_price or "0",
                    "image": product_image or "",
                    "link": product_link or "",
                }
            }