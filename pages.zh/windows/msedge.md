# msedge

> 现代网络浏览器，由微软开发，基于谷歌开发的 Chromium 网络浏览器。
> 此命令在其他平台上可作为 `microsoft-edge` 使用。
> 注意：来自 `chromium` 的额外命令参数也可以用于控制 Microsoft Edge。
> 更多信息：<https://microsoft.com/edge>。

- 打开特定的 URL 或文件：

`msedge {{https://example.com|path/to/file.html}}`

- 以 InPrivate 模式打开：

`msedge --inprivate {{example.com}}`

- 在新窗口中打开：

`msedge --new-window {{example.com}}`

- 以应用程序模式打开（没有工具栏、地址栏、按钮等）：

`msedge --app={{https://example.com}}`

- 使用代理服务器：

`msedge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 使用自定义的个人资料目录打开：

`msedge --user-data-dir={{path/to/directory}}`

- 以不进行 CORS 验证的方式打开（用于测试 API）：

`msedge --user-data-dir={{path/to/directory}} --disable-web-security`

- 为每个打开的标签页打开 DevTools 窗口：

`msedge --auto-open-devtools-for-tabs`