# notmuch

> 用于索引、搜索、阅读和标记大量电子邮件的命令行程序。
> 更多信息：<https://notmuchmail.org/manpages/>.

- 配置首次使用：

`notmuch setup`

- 为所有匹配搜索词的邮件添加标签：

`notmuch tag +{{custom_tag}} "{{search_term}}"`

- 从所有匹配搜索词的邮件中删除标签：

`notmuch tag -{{custom_tag}} "{{search_term}}"`

- 统计匹配给定搜索词的邮件数量：

`notmuch count --output={{messages|threads}} "{{search_term}}"`

- 搜索匹配给定搜索词的邮件：

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} "{{search_term}}"`

- 将搜索结果限制为 X 条：

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} --limit={{X}} "{{search_term}}"`

- 为一组邮件创建回复模板：

`notmuch reply --format={{default|headers-only}} --reply-to={{sender|all}} "{{search_term}}"`
