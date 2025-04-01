# rspamc

> 命令行客户端，用于连接 rspamd 服务器。
> 更多信息：<https://manned.org/rspamc>.

- 训练贝叶斯过滤器识别邮件为垃圾邮件：

`rspamc learn_spam {{path/to/email_file}}`

- 训练贝叶斯过滤器识别邮件为非垃圾邮件：

`rspamc learn_ham {{path/to/email_file}}`

- 生成邮件的手动报告：

`rspamc symbols {{path/to/email_file}}`

- 显示服务器统计信息：

`rspamc stat`