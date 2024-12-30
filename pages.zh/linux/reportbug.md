# reportbug

> Debian 发行版的错误报告工具。
> 更多信息：<https://manned.org/reportbug>。

- 生成关于特定软件包的错误报告，然后通过电子邮件发送：

`reportbug {{package}}`

- 报告一个不针对特定软件包的错误（一般问题、基础设施等）：

`reportbug other`

- 将错误报告写入文件，而不是通过电子邮件发送：

`reportbug -o {{filename}} {{package}}`