# npm bugs

> 在网页浏览器中报告软件包的错误。
> 尝试打开软件包的错误跟踪器 URL 或支持邮箱。
> 更多信息：<https://docs.npmjs.com/cli/npm-bugs>。

- 通过打开指定软件包的错误跟踪器来报告特定软件包的错误：

`npm bugs {{package_name}}`

- 通过搜索 `package.json` 文件并使用其名称来打开当前软件包的错误跟踪器：

`npm bugs`

- 通过设置首选浏览器来配置用于打开 URL 的浏览器：

`npm config set browser {{browser_name}}`

- 控制 URL 的打开方式：将 `browser` 设置为 `true` 以使用系统 URL 打开器，或设置为 `false` 以在终端中打印 URL：

`npm config set browser {{true|false}}`