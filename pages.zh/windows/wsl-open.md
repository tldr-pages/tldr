# wsl-open

> 在 Windows 子系统 Linux 中从用户默认的 Windows GUI 应用程序打开文件或 URL。
> 更多信息：<https://gitlab.com/4U6U57/wsl-open>。

- 在 Windows 资源管理器中打开当前目录：

`wsl-open {{.}}`

- 在用户默认的 Windows 网页浏览器中打开 URL：

`wsl-open {{https://example.com}}`

- 在用户默认的 Windows 应用程序中打开特定文件：

`wsl-open {{path\to\file}}`

- 将 `wsl-open` 设置为 shell 的网页浏览器（使用 `wsl-open` 打开链接）：

`wsl-open -w`

- 显示帮助信息：

`wsl-open -h`