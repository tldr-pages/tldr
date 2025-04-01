# urpmq

> 查询 Mageia 中软件包和介质的信息。
> 参见: `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpme`。
> 更多信息：<https://wiki.mageia.org/en/URPMI#urpmq>。

- 显示可安装软件包的信息：

`urpmq -i {{package}}`

- 显示软件包的直接依赖关系：

`urpmq --requires {{package}}`

- 显示软件包的直接和间接依赖关系：

`urpmq --requires-recursive {{package}}`

- 列出需要的 RPM 文件的未安装软件包及其来源：

`sudo urpmq --requires-recursive -m --sources {{path/to/file.rpm}}`

- 列出所有已配置的介质及其 URL，包括未激活的介质：

`urpmq --list-media --list-url`

- 搜索软件包，打印其 [g]roup、version 和 [r]elease：

`urpmq -g -r --fuzzy {{keyword}}`

- 使用软件包的确切名称搜索：

`urpmq -g -r {{package}}`