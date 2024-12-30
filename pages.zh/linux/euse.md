# euse

> 启用、禁用和获取有关 Gentoo USE 标志的信息。 
> 更多信息请访问：<https://wiki.gentoo.org/wiki/Euse>。

- 列出活动的全局 USE 标志：

`euse --active --global`

- 列出活动的本地 USE 标志：

`euse --active --local`

- 启用一个全局 USE 标志：

`sudo euse --enable {{use_flag}}`

- 禁用一个全局 USE 标志（在 USE 标志前加上 '-' 符号）：

`sudo euse --disable {{use_flag}}`

- 移除一个全局 USE 标志：

`sudo euse --prune {{use_flag}}`