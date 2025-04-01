# eix

> 用于搜索本地 Gentoo 包的工具。
> 使用 `eix-update` 更新本地包缓存。
> 更多信息：<https://wiki.gentoo.org/wiki/Eix>。

- 搜索包：

`eix {{query}}`

- 搜索已安装的包：

`eix --installed {{query}}`

- 在包描述中搜索：

`eix --description "{{description}}"`

- 按包许可搜索：

`eix --license {{license}}`

- 从搜索结果中排除：

`eix --not --license {{license}}`
