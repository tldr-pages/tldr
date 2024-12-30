# archwiki-rs

> 从 ArchWiki 中读取、搜索和下载页面。
> 更多信息：<https://gitlab.com/lucifayr/archwiki-rs>。

- 从 ArchWiki 中读取一个页面：

`archwiki-rs read-page {{页面标题}}`

- 以指定格式从 ArchWiki 中读取一个页面：

`archwiki-rs read-page {{页面标题}} --format {{纯文本|markdown|html}}`

- 在 ArchWiki 中搜索包含提供文本的页面：

`archwiki-rs search "{{搜索文本}}" --text-search`

- 将所有 ArchWiki 页面下载到指定目录的本地副本：

`archwiki-rs local-wiki {{/path/to/local_wiki}} --format {{纯文本|markdown|html}}`