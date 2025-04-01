# eol

> 显示多个产品的生命周期结束日期（EoL）。
> 更多信息：<https://github.com/hugovk/norwegianblue>.

- 列出所有可用的产品：

`eol`

- 获取一个或多个产品的EoL日期：

`eol {{product1 product2 ...}}`

- 打开产品网页：

`eol {{product}} --web`

- 以特定格式获取一个或多个产品的EoL日期：

`eol {{product1 product2 ...}} --format {{html|json|md|markdown|pretty|rst|csv|tsv|yaml}}`

- 将一个或多个产品的EoL日期导出为单个Markdown文件：

`eol {{product1 product2 ...}} --format {{markdown}} > {{eol_report.md}}`

- 显示帮助：

`eol --help`
