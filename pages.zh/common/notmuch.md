# notmuch

> 基于命令行的程序，用于索引、搜索、阅读和标记大量电子邮件消息。
> 更多信息请访问：<https://notmuchmail.org/manpages/>。

- 首次使用时进行配置：

`notmuch setup`

- 为所有匹配搜索词的消息添加标签：

`notmuch tag +{{custom_tag}} "{{search_term}}"`

- 为所有匹配搜索词的消息移除标签：

`notmuch tag -{{custom_tag}} "{{search_term}}"`

- 计算匹配给定搜索词的消息数量：

`notmuch count --output={{messages|threads}} "{{search_term}}"`

- 搜索匹配给定搜索词的消息：

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} "{{search_term}}"`

- 将搜索结果数量限制为X：

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} --limit={{X}} "{{search_term}}"`

- 为一组消息创建回复模板：

`notmuch reply --format={{default|headers-only}} --reply-to={{sender|all}} "{{search_term}}"`