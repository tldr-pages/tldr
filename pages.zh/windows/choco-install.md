# choco install

> 使用 Chocolatey 下载一个或多个包。
> 更多信息：<https://chocolatey.org/docs/commands-install>.

- 安装一个或多个用空格分隔的软件包：

`choco install {{包名 包名 ..}}`

- 从一个自定义的配置文件中安装包：

`choco install {{配置文件的路径}}`

- 安装一个特定的 "nuspec" 或 "nupkg" 文件：

`choco install {{文件的路径}}`

- 安装一个指定版本的包：

`choco install {{包名}} --version {{版本号}}`

- 允许安装一个包的多个版本：

`choco install {{包名}} --allow-multiple`

- 自动确认所有提示：

`choco install {{包名}} --yes`

- 从自定义的源处获取包：

`choco install {{包名}} --source {{源 URL|别名}}`

- 提供一个用户名和密码来进行验证：

`choco install {{包名}} --user {{用户名}} --password {{密码}}`
