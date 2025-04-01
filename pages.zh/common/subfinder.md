# subfinder

> 发现网站的有效子域。
> 设计为被动框架，适用于漏洞赏金和渗透测试。
> 更多信息：<https://github.com/projectdiscovery/subfinder>。

- 为特定域名查找子域：

`subfinder {{[-d|-domain]}} {{example.com}}`

- 仅显示找到的子域：

`subfinder -silent {{[-d|-domain]}} {{example.com}}`

- 仅显示活跃的子域：

`subfinder {{[-nW|-active]}} {{[-d|-domain]}} {{example.com}}`

- 使用所有数据源进行枚举：

`subfinder -all {{[-d|-domain]}} {{example.com}}`

- 使用给定的逗号分隔的 [r]esolvers 列表：

`subfinder -r {{8.8.8.8,1.1.1.1,...}} {{[-d|-domain]}} {{example.com}}`
