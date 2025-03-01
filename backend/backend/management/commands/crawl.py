from spiders.amazon import AmazonSpider
from spiders.bewakoof import BewakoofSpider
from scrapy.crawler import CrawlerProcess
from django.core.management.base import BaseCommand
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Run the Amazon or Bewakoof spider"

    def add_arguments(self, parser):
        parser.add_argument("website", type=str, choices=['amazon', 'bewakoof'], 
                          help="Website to crawl (amazon or bewakoof)")
        parser.add_argument("category", type=str, help="Category to crawl")
        parser.add_argument(
            "--save-to-db",
            action="store_true",
            default=False,
            help="Save results to database"
        )

    def handle(self, *args, **options):
        website = options["website"]
        category = options["category"]
        save_to_db = options["save_to_db"]
        
        self.stdout.write(
            self.style.SUCCESS(f'Starting {website} crawler for category: {category}')
        )
        if save_to_db:
            self.stdout.write(
                self.style.SUCCESS('Results will be saved to database')
            )
            
        process = CrawlerProcess(get_project_settings())
        
        # Choose spider based on website argument
        spider_class = AmazonSpider if website == 'amazon' else BewakoofSpider
        process.crawl(spider_class, category=category, save_to_db=save_to_db)
        process.start()
