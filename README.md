# drf-api-isu

This is an api that represents the ability to search for jobs and services. The server also provides an opportunity to post your resume.
A feature of the server api is the use of full-text search to search for anything on the site. In addition to full-text search, the api also supports search with parameters.
You can create an add-on to the api in the form of a web application, a telegram bot, or in another form.
Ease of use is created by docker-compose.
The api uses for its work:
- PostgreSQL (for data storage)
- Elasticsearch (for full-text search)
- Redis (as a broker and for hash storage)
- Celery
Flower and Redisinsight are also used for data analytics
