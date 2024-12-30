# eselect 新闻

> 一个用于读取 Gentoo 新闻项的 `eselect` 模块。
> 注意：当一个仓库同步时且有未读的新闻项时，Portage 将打印通知。
> 更多信息：<https://wiki.gentoo.org/wiki/Eselect#News>。

- 列出可用的新闻项及其编号（默认情况下为全部）：

`eselect news list {{all|new}}`

- 打印指定的新闻项：

`eselect news read {{number1 number2 ...}}`

- 打印所有未读的新闻项：

`eselect news read`

- 将指定的新闻项标记为未读：

`eselect news unread {{number1 number2 ...}}`

- 删除所有已读的新闻项：

`eselect news purge`

- 打印可用新闻项的数量（默认情况下为新）：

`eselect news count {{all|new}}`