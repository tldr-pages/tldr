# choco 安装

> 使用 Chocolatey 安装一个或多个软件包。
> 更多信息：<https://chocolatey.org/docs/commands-install>。

- 安装一个或多个软件包：

`choco install {{package1 package2 ...}}`

- 从自定义配置文件安装软件包：

`choco install {{path\to\packages_file.config}}`

- 安装特定的 `nuspec` 或 `nupkg` 文件：

`choco install {{path\to\file}}`

- 安装软件包的特定版本：

`choco install {{package}} --version {{version}}`

- 允许安装软件包的多个版本：

`choco install {{package}} --allow-multiple`

- 自动确认所有提示：

`choco install {{package}} --yes`

- 指定一个自定义源以接收软件包：

`choco install {{package}} --source {{source_url|alias}}`

- 提供用户名和密码进行身份验证：

`choco install {{package}} --user {{username}} --password {{password}}`