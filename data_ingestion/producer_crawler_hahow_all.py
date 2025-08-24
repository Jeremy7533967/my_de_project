from data_ingestion.tasks_crawler_hahow_course import crawler_hahow_course
from data_ingestion.tasks_crawler_hahow_article import crawler_hahow_article

categories = ["programming", "marketing", "language"]

for category in categories:
    crawler_hahow_course.delay(category=category)
    crawler_hahow_article.delay(category=category)