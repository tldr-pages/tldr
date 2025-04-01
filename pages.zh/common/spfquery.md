# spfquery

> 查询发件人策略框架记录以验证电子邮件发件人。
> 更多信息：<https://manned.org/spfquery>.

- 检查某个 IP 地址是否被允许从指定的电子邮件地址发送电子邮件：

`spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}}`

- 打开调试输出：

`spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}} --debug`
