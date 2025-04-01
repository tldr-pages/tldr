# xwininfo

> 显示窗口信息。
> 另见：`xprop`, `xkill`。
> 更多信息：<https://www.x.org/releases/current/doc/man/man1/xwininfo.1.xhtml>。

- 显示一个光标以选择窗口并显示其属性（ID、名称、大小、位置等）：

`xwininfo`

- 显示所有窗口的树形结构：

`xwininfo -tree -root`

- 显示具有特定ID的窗口的属性：

`xwininfo -id {{id}}`

- 显示具有特定名称的窗口的属性：

`xwininfo -name {{name}}`

- 通过名称搜索并显示窗口的ID：

`xwininfo -tree -root | grep {{keyword}} | head -1 | perl -ne 'print $1 if /(0x[\da-f]+)/ig;'`
