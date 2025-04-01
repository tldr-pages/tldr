# euse

> 启用、禁用和获取关于 Gentoo USE 标记的信息。
> 更多信息：<https://wiki.gentoo.org/wiki/Euse>.

- 列出活跃的全局 USE 标记：

`euse --active --global`

- 列出活跃的局部 USE 标记：

`euse --active --local`

- 启用全局 USE 标记：

`sudo euse --enable {{use_flag}}`

- 禁用全局 USE 标记（在 USE 标记前加上 '-' 符号）：

`sudo euse --disable {{use_flag}}`

- 移除全局 USE 标记：

`sudo euse --prune {{use_flag}}`