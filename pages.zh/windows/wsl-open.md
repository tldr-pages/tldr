# wsl-open

> 在 Windows Subsystem for Linux 中使用用户的默认 Windows GUI 应用程序打开文件或 URL。
> 更多信息：<https://gitlab.com/4U6U57/wsl-open>。

- 在 Windows 资源管理器中打开当前目录：

`wsl-open {{.}}`

- 在 Windows 中使用用户的默认网络浏览器打开 URL：

`wsl-open {{https://example.com}}`

- 在 Windows 中使用用户的默认应用程序打开特定文件：

`wsl-open {{path\to\file}}`

- 设置 `wsl-open` 为 shell 的网络浏览器（使用 `wsl-open` 打开链接）：

`wsl-open -w`

- 显示帮助：

`wsl-open -h`