# npm bugs

> 在网页浏览器中报告软件包的错误。
> 尝试打开软件包的错误跟踪网址或支持电子邮件。
> 更多信息：<https://docs.npmjs.com/cli/npm-bugs>。

- 通过打开指定软件包的错误跟踪器来报告特定软件包的错误：

`npm bugs {{package_name}}`

- 通过搜索 `package.json` 文件并使用其名称打开当前软件包的错误跟踪器：

`npm bugs`

- 通过为 `npm` 命令设置您首选的浏览器来配置用于打开网址的浏览器：

`npm config set browser {{browser_name}}`

- 控制网址打开行为：将 `browser` 设置为 `true` 以使用系统网址打开器，或设置为 `false` 以在终端中打印网址：

`npm config set browser {{true|false}}`