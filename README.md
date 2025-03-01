🛍️ SHOPPIN - E-commerce Product Crawler
=====================================

📦 What is this?
--------------
A Django-based web crawler that fetches product data from e-commerce websites (currently Amazon and Bewakoof.com). Built for learning and demonstration purposes!

🔧 Tech Stack
-----------
• 🐍 Python & Django - Core backend
• 🕷️ Scrapy - Web crawling
• 🎭 Selenium - Browser automation
• 🐳 Docker - Containerization
• 📮 Redis & Celery - Task processing
• 🗄️ SQLite - Database

🚀 Quick Start
------------
1. Clone the repo
2. Run Docker services:
   ```bash
   docker-compose up -d
   ```
3. Start crawling:
   ```bash
   poetry run python manage.py crawl [amazon|bewakoof] [category] --save-to-db
   ```

📂 Project Structure
-----------------
• 🕷️ /spiders - Crawler implementations
• 📊 /crawler - Django app for data models
• 🎮 /management - CLI commands
• 🐳 docker-compose.yaml - Service orchestration

✨ Features
---------
• 🤖 Multi-site crawling support
• ♾️ Infinite scroll handling
• 🗃️ Automatic data storage
• 🎯 Category-based crawling
• 📊 Admin dashboard
• 🐋 Containerized services

⚠️ Current Limitations
-------------------
• 🐞 Alpha version (0.1.0)
• 💔 Fragile HTML selectors
• 📉 Basic error handling
• 🏋️ Limited scalability
• 🔄 No automatic updates

👥 Who's it for?
--------------
• 🎓 Learning web crawling
• 🔬 Testing crawler concepts
• 🧪 Development purposes
• 📚 Educational projects

🔜 Future Plans
-------------
• 🔄 Better error handling
• 🚀 Performance optimization
• 📊 Data analytics
• 🔐 Security improvements
• 🌐 More e-commerce sites
