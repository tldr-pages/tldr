# microsoft-edge

> 由微软开发的现代网络浏览器，基于谷歌开发的 Chromium 浏览器。
> 此命令在 Windows 系统中也可作为 `msedge` 使用。
> 注意：Chromium 的其他命令参数也可能用于控制 Microsoft Edge。
> 更多信息：<https://microsoft.com/edge>.

- 打开特定的 URL 或文件：

`microsoft-edge {{https://example.com|path/to/file.html}}`

- 以 InPrivate 模式打开：

`microsoft-edge --inprivate {{example.com}}`

- 在新窗口中打开：

`microsoft-edge --new-window {{example.com}}`

- 以应用模式打开（无工具栏、地址栏、按钮等）：

`microsoft-edge --app={{https://example.com}}`

- 使用代理服务器：

`microsoft-edge --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 使用自定义用户数据目录打开：

`microsoft-edge --user-data-dir={{path/to/directory}}`

- 无 CORS 验证打开（用于测试 API）：

`microsoft-edge --user-data-dir={{path/to/directory}} --disable-web-security`

- 打开时为每个标签页自动打开 DevTools 窗口：

`microsoft-edge --auto-open-devtools-for-tabs`
