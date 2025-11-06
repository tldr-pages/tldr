# dex

> DesktopEntry Execution 是一个用于生成和执行 Application 类型的 DesktopEntry 文件的程序。
> 更多信息：<https://github.com/jceb/dex>.

- 执行自动启动文件夹中的所有程序：

`dex {{[-a|--autostart]}}`

- 执行指定文件夹中的所有程序：

`dex {{[-a|--autostart]}} {{[-s|--search-paths]}} {{路径/到/目录1}}:{{路径/到/目录2}}:{{路径/到/目录3}}`

- 预览在 GNOME 特定自动启动中将会执行的程序：

`dex {{[-a|--autostart]}} {{[-e|--environment]}} {{GNOME}}`

- 预览在常规自动启动中将会执行的程序：

`dex {{[-a|--autostart]}} {{[-d|--dry-run]}}`

- 预览 DesktopEntry 属性 Name 的值：

`dex {{[-p|--property]}} {{Name}} {{路径/到/文件.desktop}}`

- 为当前目录中的程序创建 DesktopEntry：

`dex {{[-c|--create]}} {{路径/到/文件.desktop}}`

- 在给定的终端中执行单个程序（桌面文件中 Terminal=true）：

`dex --term {{terminal}} {{路径/到/文件.desktop}}`
