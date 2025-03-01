🛍️ SHOPPIN - E-commerce Product Crawler
=====================================

What is this?
------------
A Django-based web crawler that fetches product data from e-commerce websites (Amazon and Bewakoof.com). Built for learning and demonstration purposes.

🔧 Tech Stack
-----------
- Python & Django - Core backend
- Scrapy - Web crawling
- Selenium - Browser automation
- Docker - Containerization
- Redis & Celery - Task queue
- SQLite - Database

Quick Start
----------
1. Clone the repo
2. Start services:
   ```bash
   docker-compose up -d
   ```
3. Run crawler:
   ```bash
   poetry run python manage.py crawl [amazon|bewakoof] [category] --save-to-db
   ```

Project Structure
---------------
/backend
  ├── /spiders           # Crawler implementations
  ├── /crawler           # Django app & models
  ├── /management        # CLI commands
  └── docker-compose.yaml # Service configuration

Key Features
-----------
• Multi-site crawling
• Infinite scroll handling
• Automatic data storage
• Category-based crawling
• Admin dashboard
• Containerized services

⚠️ Current Status
---------------
• Alpha version (0.1.0)
• Development build
• Basic error handling
• Limited scalability
• Requires monitoring

Development Setup
---------------
1. Requirements:
   • Docker & Docker Compose
   • Python 3.13
   • Poetry

2. Environment:
   • Copy .env.example to .env
   • Configure database settings
   • Set up admin credentials

3. Dependencies:
   ```bash
   poetry install
   ```

Usage Examples
------------
# Start all services
docker-compose up -d

# Crawl products
poetry run python manage.py crawl amazon electronics --save-to-db
poetry run python manage.py crawl bewakoof tshirts --save-to-db

# Access admin interface
http://localhost:8000/admin

Future Plans
-----------
• Error handling improvements
• Performance optimization
• Data validation
• Security enhancements
• Additional e-commerce sites

Note
----
This is a development version meant for learning and testing. Expect frequent updates and potential breaking changes.

License
-------
MIT License