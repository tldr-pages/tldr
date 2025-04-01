# rss2email

> 将 RSS 源中的新闻递送到电子邮件程序中。
> 更多信息：<https://github.com/rss2email/rss2email>。

- 列出所有订阅源：

`r2e list`

- 将 RSS 条目转换为电子邮件：

`r2e run`

- 添加一个订阅源：

`r2e add {{feed_address}}`

- 使用特定的电子邮件地址添加订阅源：

`r2e add {{feed_address}} {{new_email@example.com}}`

- 删除特定的订阅源：

`r2e delete {{number_of_feed_in_list}}`

- 显示帮助：

`r2e -h`