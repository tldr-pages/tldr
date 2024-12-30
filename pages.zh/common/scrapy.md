# scrapy

> 网络爬虫框架。
> 更多信息：<https://scrapy.org>。

- 创建一个项目：

`scrapy startproject {{project_name}}`

- 创建一个爬虫（在项目目录中）：

`scrapy genspider {{spider_name}} {{website_domain}}`

- 编辑爬虫（在项目目录中）：

`scrapy edit {{spider_name}}`

- 运行爬虫（在项目目录中）：

`scrapy crawl {{spider_name}}`

- 按照 Scrapy 看到的方式获取网页并将源代码打印到 `stdout`：

`scrapy fetch {{url}}`

- 按照 Scrapy 看到的方式在默认浏览器中打开网页（禁用 JavaScript 以提高准确性）：

`scrapy view {{url}}`

- 为 URL 打开 Scrapy shell，这允许在 Python shell（如果可用，则为 IPython）中与页面源进行交互：

`scrapy shell {{url}}`