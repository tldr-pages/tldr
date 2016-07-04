# scrapy

> Open Source framework for crawling websites written in python.

- Create a project:

`scrapy startproject {{project_name}}`

- Create a spider:

`scrapy genspider {{spider_name}} {{website_domain}}`

- Edit spider:

`scrapy edit {{spider_name}}`

- Run spider:

`scrapy crawl {{spider_name}}`

- Fetch a webpage as scrapy sees it and print source in stdout:

`scrapy fetch {{url}}`

- View a webpage as scrapy sees it, opens it in browser(disable javascript before):

`scrapy view {{url}}`

- Open scrapy shell for url, which allows you to interact with the page source in python shell:

`scrapy shell {{url}}` 

