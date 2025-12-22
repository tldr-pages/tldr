# archwiki-rs

> 从 ArchWiki 阅读、搜索并下载页面。
> 更多信息：<https://gitlab.com/lucifayr/archwiki-rs>.

- 从 ArchWiki 阅读一个页面：

`archwiki-rs read-page {{页面标题}}`

- 以指定格式从 ArchWiki 阅读一个页面：

`archwiki-rs read-page {{页面标题}} --format {{plain-text|markdown|html}}`

- 在 ArchWiki 中搜索包含所提供文本的页面：

`archwiki-rs search "{{搜索文本}}" --text-search`

- 将所有 ArchWiki 页面下载到指定目录中的本地副本：

`archwiki-rs local-wiki /{{路径/到/本地_wiki}} --format {{plain-text|markdown|html}}`
