# vkpurge

> 列出或移除由 `xbps` 留下的旧内核版本。
> `version` 参数支持 shell 通配符。
> 更多信息：<https://man.voidlinux.org/vkpurge.8>。

- 列出所有可移除的内核版本（如果指定了参数，则列出匹配 `version` 的内核版本）：

`vkpurge list {{version}}`

- 移除所有未使用的内核：

`vkpurge rm all`

- 移除匹配 `version` 的内核版本：

`vkpurge rm {{version}}`