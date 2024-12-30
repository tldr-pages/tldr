# urpmq

> 查询Mageia中的软件包和媒体信息。
> 另见：`urpmi`，`urpmi.update`，`urpmi.addmedia`，`urpmi.removemedia`，`urpmf`，`urpme`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmq>。

- 显示可安装软件包的信息：

`urpmq -i {{package}}`

- 显示软件包的直接依赖项：

`urpmq --requires {{package}}`

- 显示软件包的直接和间接依赖项：

`urpmq --requires-recursive {{package}}`

- 列出RPM文件所需但未安装的软件包及其来源：

`sudo urpmq --requires-recursive -m --sources {{path/to/file.rpm}}`

- 列出所有已配置的媒体及其URL，包括非活动媒体：

`urpmq --list-media --list-url`

- 搜索软件包并打印[g]组，版本和[r]发布：

`urpmq -g -r --fuzzy {{keyword}}`

- 使用软件包的确切名称搜索软件包：

`urpmq -g -r {{package}}`