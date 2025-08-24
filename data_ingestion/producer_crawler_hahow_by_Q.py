from data_ingestion.tasks_crawler_hahow_course import crawler_hahow_course
from data_ingestion.tasks_crawler_hahow_article import crawler_hahow_article

categories = ["programming", "marketing", "language"]

for category in categories:
    crawler_hahow_course.apply_async(
        kwargs={'category': category},
        queue='hahow_course'
        )
    print(f"Send hahow_course task, category: {category}")
    crawler_hahow_article.apply_async(
       kwargs={'category': category},
       queue='hahow_article'
       )
    print(f"Send hahow_article task, category: {category}")