# subfinder

> 发现网站的有效子域名。
> 设计为一种被动框架，方便用于漏洞赏金项目，并且安全用于渗透测试。
> 更多信息：<https://github.com/projectdiscovery/subfinder>。

- 为特定 [d]omain 查找子域名：

`subfinder -d {{example.com}}`

- 仅显示找到的子域名：

`subfinder -silent -d {{example.com}}`

- 仅显示活动子域名：

`subfinder -nW -d {{example.com}}`

- 使用所有来源进行枚举：

`subfinder -all -d {{example.com}}`

- 使用给定的逗号分隔的 [r]esolvers 列表：

`subfinder -r {{8.8.8.8,1.1.1.1,...}} -d {{example.com}}`