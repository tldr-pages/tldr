# msedge

> 由 Microsoft 基于 Google 开发的 Chromium 浏览器构建的现代网页浏览器。
> 在其他平台上，此命令可能以 `microsoft-edge` 的形式提供。
> 注意：来自 `chromium` 的附加命令参数也可以用于控制 Microsoft Edge。
> 更多信息：<https://microsoft.com/edge>.

- 打开特定的 URL 或文件：

`msedge {{https://example.com|path/to/file.html}}`

- 在 InPrivate 模式下打开：

`msedge --inprivate {{example.com}}`

- 在新窗口中打开：

`msedge --new-window {{example.com}}`

- 以应用模式打开（无工具栏、URL 栏、按钮等）：

`msedge --app={{https://example.com}}`

- 使用代理服务器：

`msedge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 使用自定义用户数据目录打开：

`msedge --user-data-dir={{path/to/directory}}`

- 无 CORS 验证打开（用于测试 API）：

`msedge --user-data-dir={{path/to/directory}} --disable-web-security`

- 以每个标签页打开一个 DevTools 窗口：

`msedge --auto-open-devtools-for-tabs`
