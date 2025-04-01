# eselect news

> 用于阅读 Gentoo 新闻项目的 `eselect` 模块。
> 注意：Portage 将在存储库同步时，如果有未读新闻项目，会显示提示信息。
> 更多信息：<https://wiki.gentoo.org/wiki/Eselect#News>。

- 列出可用的新闻项目及其编号（默认为全部）：

`eselect news list {{all|new}}`

- 打印指定的新闻项目：

`eselect news read {{number1 number2 ...}}`

- 打印所有未读的新闻项目：

`eselect news read`

- 将指定的新闻项目标记为未读：

`eselect news unread {{number1 number2 ...}}`

- 删除所有已读的新闻项目：

`eselect news purge`

- 打印可用的新闻项目数量（默认为新的）：

`eselect news count {{all|new}}`