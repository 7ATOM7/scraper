# scraper
A docker implementation of a Scraper which scrapes books_to_scrape and writes to a postgres db in another container. The web site http://books.toscrape.com/ is giving connection time out frequently. Server is refusing to send return packets. Hence the final output in db is provided as csv in the scraper Folder. Connect to db from your local machine as local host as host and port 5432
Username and password of DB is postgres and postgres.

Use docker-compose up for starting the service.

