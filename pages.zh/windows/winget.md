# winget

> Windows 软件包管理器。
> 更多信息: <https://learn.microsoft.com/windows/package-manager/winget>。

- 安装一个软件包：

`winget install {{package}}`

- 移除一个软件包（注意：可以使用 `remove` 来替代 `uninstall`）：

`winget uninstall {{package}}`

- 显示一个软件包的信息：

`winget show {{package}}`

- 搜索一个软件包：

`winget search {{package}}`

- 将所有软件包升级到最新版本：

`winget upgrade --all`

- 列出所有可以用 `winget` 管理的已安装软件包：

`winget list --source winget`

- 从文件导入软件包，或将已安装的软件包导出到文件：

`winget {{import|export}} {{--import-file|--output}} {{path/to/file}}`

- 在提交 PR 到 winget-pkgs 仓库之前验证清单：

`winget validate {{path/to/manifest}}`