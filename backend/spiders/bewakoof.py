import time
import scrapy
from crawler.models import BewakoofProduct
from scrapy_selenium import SeleniumRequest

from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # example


class BewakoofSpider(scrapy.Spider):
    name = "bewakoof"
    start_urls = ["https://www.bewakoof.com/"]

    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.bewakoof.com/men-clothing",
            callback=self.parse,
            wait_time=5,  # Initial wait time
            screenshot=True,
            dont_filter=True,
        )

    def parse(self, response):
        driver = webdriver.Remote("http://127.0.0.1:4444", options=options)

        total_products = int(
            response.xpath(
                "/html/body/div/main/main/div[2]/div/main/div/section[2]/div[1]/div[1]/div/span/text()"
            ).get()
        )

        items = {}
        products_found = 0
        last_height = driver.execute_script("return document.body.scrollHeight")

        while products_found < total_products:
            # Scroll to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new content to load

            # Get new scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # Parse visible products
            products = response.css("section.sc-89d6e897-4.FQouP")
            for product in products:
                item = self.parse_item(product)
                if item:
                    items.update(item)
                    products_found += 1

            # Break if no more new content (reached bottom or hit limit)
            if new_height == last_height:
                break
            last_height = new_height

            self.logger.info(f"Found {products_found} products out of {total_products}")

        yield items

    def parse_item(self, product):
        name = product.css("span.fjEpcQ::text").get()
        price = product.css("span.jPdKrZ::text").get()
        image = product.css("img::attr(src)").get()
        link = product.css("a::attr(href)").get()

        if name:
            if self.save_to_db:
                BewakoofProduct.objects.get_or_create(
                    name=name,
                    defaults={
                        "price": price.replace("₹", "") if price else "0",
                        "image_url": image,
                        "product_link": (
                            f"https://www.bewakoof.com{link}" if link else ""
                        ),
                        "category": self.category,
                    },
                )

            return {
                name.strip(): {
                    "price": price.replace("₹", "") if price else "0",
                    "image": image or "",
                    "link": f"https://www.bewakoof.com{link}" if link else "",
                }
            }
