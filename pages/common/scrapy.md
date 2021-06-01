# scrapy

> Web-crawling framework.
> More information: <https://scrapy.org>.

- Create a project:

`scrapy startproject {{project_name}}`

- Create a spider (in project directory):

`scrapy genspider {{spider_name}} {{website_domain}}`

- Edit spider (in project directory):

`scrapy edit {{spider_name}}`

- Run spider (in project directory):

`scrapy crawl {{spider_name}}`

- Fetch a webpage as Scrapy sees it and print source in stdout:

`scrapy fetch {{url}}`

- Open a webpage in the default browser as Scrapy sees it (disable JavaScript for extra fidelity):

`scrapy view {{url}}`

- Open Scrapy shell for URL, which allows interaction with the page source in python shell (or ipython if available):

`scrapy shell {{url}}`
