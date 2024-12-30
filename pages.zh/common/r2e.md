# r2e

> 将 RSS 源转发到电子邮件地址。
> 需要配置好的 `sendmail` 或 smtp 设置。
> 更多信息：<https://github.com/rss2email/rss2email>。

- 创建一个新的源数据库，将电子邮件发送到电子邮件地址：

`r2e new {{email_address}}`

- 订阅一个源：

`r2e add {{feed_name}} {{feed_URI}}`

- 将新故事发送到电子邮件地址：

`r2e run`

- 列出所有源：

`r2e list`

- 删除指定索引的源：

`r2e delete {{index}}`