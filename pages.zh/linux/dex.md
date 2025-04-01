# dex

> DesktopEntry Execution 是一个用于生成和执行 Application 类型 DesktopEntry 文件的程序。
> 更多信息：<https://github.com/jceb/dex>.

- 执行所有自动启动文件夹中的程序：

`dex --autostart`

- 执行指定文件夹中的所有程序：

`dex --autostart --search-paths {{path/to/directory1}}:{{path/to/directory2}}:{{path/to/directory3}}:`

- 预览 GNOME 特定自动启动中的程序：

`dex --autostart --environment {{GNOME}}`

- 预览常规自动启动中的程序：

`dex --autostart --dry-run`

- 预览 DesktopEntry 属性 `Name` 的值：

`dex --property {{Name}} {{path/to/file.desktop}}`

- 在当前目录中为程序创建一个 DesktopEntry：

`dex --create {{path/to/file.desktop}}`

- 在指定的终端中执行单个程序（在桌面文件中 `Terminal=true`）：

`dex --term {{terminal}} {{path/to/file.desktop}}`
