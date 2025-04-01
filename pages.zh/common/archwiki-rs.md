# archwiki-rs

> 从 ArchWiki 读取、搜索和下载页面。
> 更多信息：<https://gitlab.com/lucifayr/archwiki-rs>。

- 从 ArchWiki 读取页面：

`archwiki-rs read-page {{page_title}}`

- 以指定格式从 ArchWiki 读取页面：

`archwiki-rs read-page {{page_title}} --format {{plain-text|markdown|html}}`

- 搜索包含提供文本的 ArchWiki 页面：

`archwiki-rs search "{{search_text}}" --text-search`

- 将所有 ArchWiki 页面的本地副本下载到指定目录：

`archwiki-rs local-wiki {{/path/to/local_wiki}} --format {{plain-text|markdown|html}}`