# rspamc

> rspamd 服务器的命令行客户端。
> 更多信息请访问：<https://manned.org/rspamc>。

- 训练贝叶斯过滤器将电子邮件识别为垃圾邮件：

`rspamc learn_spam {{path/to/email_file}}`

- 训练贝叶斯过滤器将电子邮件识别为正常邮件：

`rspamc learn_ham {{path/to/email_file}}`

- 生成电子邮件的手动报告：

`rspamc symbols {{path/to/email_file}}`

- 显示服务器统计信息：

`rspamc stat`