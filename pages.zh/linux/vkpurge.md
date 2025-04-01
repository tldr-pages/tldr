# vkpurge

> 列出或删除 `xbps` 留下的旧内核版本。
> `version` 参数支持 shell 通配符。
> 更多信息：<https://man.voidlinux.org/vkpurge.8>。

- 列出所有可删除的内核版本（如果指定了 `version` 参数，则列出匹配的内核版本）：

`vkpurge list {{version}}`

- 删除所有未使用的内核：

`vkpurge rm all`

- 删除匹配 `version` 的内核版本：

`vkpurge rm {{version}}`
