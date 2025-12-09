# winget

> Windows 软件包管理器命令行工具。
> 更多信息：<https://learn.microsoft.com/windows/package-manager/winget>.

- 安装一个包：

`winget install {{包}}`

- 移除一个包（注意：`remove` 也可以用来代替 `uninstall`）：

`winget uninstall {{包}}`

- 显示一个包的信息：

`winget show {{包}}`

- 搜索一个包：

`winget search {{包}}`

- 将所有包升级到最新版本：

`winget upgrade --all`

- 列出所有可以通过 `winget` 管理的已安装包：

`winget list --source winget`

- 从文件导入包，或将已安装的包导出到文件：

`winget {{import|export}} {{--import-file|--output}} {{路径/到/文件}}`

- 在提交合并到 winget-pkgs 仓库之前验证清单：

`winget validate {{路径/到/清单}}`
