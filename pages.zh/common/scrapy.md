# scrapy

> Web 爬取框架。
> 更多信息：<https://docs.scrapy.org/en/latest/topics/commands.html#using-the-scrapy-tool>.

- 创建一个项目：

`scrapy startproject {{项目名}}`

- 创建一个爬虫（在项目目录下）：

`scrapy genspider {{爬虫名}} {{站点域名}}`

- 编辑爬虫（在项目目录下）：

`scrapy edit {{爬虫名}}`

- 运行爬虫（在项目目录下）：

`scrapy crawl {{爬虫名}}`

- 抓取一个网页并将它的网页源码打印至标准输出：

`scrapy fetch {{url}}`

- 使用默认浏览器打开给定的 URL 来确认是否符合期望（为确保准确会禁用 JavaScript）：

`scrapy view {{url}}`

- 通过给定的 URL 打开交互窗口，除此之外还支持 UNIX 风格的本地文件路径：

`scrapy shell {{url}}`
