# 终止支持

> 显示多个产品的终止支持日期（EoLs）。
> 更多信息：<https://github.com/hugovk/norwegianblue>。

- 列出所有可用产品：

`eol`

- 获取一个或多个产品的终止支持日期：

`eol {{product1 product2 ...}}`

- 打开产品网页：

`eol {{product}} --web`

- 以特定格式获取一个或多个产品的终止支持日期：

`eol {{product1 product2 ...}} --format {{html|json|md|markdown|pretty|rst|csv|tsv|yaml}}`

- 将一个或多个产品的终止支持日期作为单个 markdown 文件获取：

`eol {{product1 product2 ...}} --format {{markdown}} > {{eol_report.md}}`

- 显示帮助信息：

`eol --help`