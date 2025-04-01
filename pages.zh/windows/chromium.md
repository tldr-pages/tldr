# chromium

> 开源浏览器，主要由 Google 开发和维护。
> 注意：您可能需要将 `chromium` 命令替换为您首选的浏览器，例如 `brave`、`google-chrome`、`microsoft-edge`/`msedge`、`opera` 或 `vivaldi`。
> 更多信息：<https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- 打开特定的 URL 或文件：

`chromium {{https://example.com|path/to/file.html}}`

- 以隐私模式打开（Microsoft Edge 使用 `--inprivate`）：

`{{chromium --incognito|msedge --inprivate}} {{example.com}}`

- 在新窗口中打开：

`chromium --new-window {{example.com}}`

- 以应用模式打开（无工具栏、URL 栏、按钮等）：

`chromium --app={{https://example.com}}`

- 使用代理服务器：

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 使用自定义配置文件目录打开：

`chromium --user-data-dir={{path/to/directory}}`

- 无 CORS 验证打开（用于测试 API）：

`chromium --user-data-dir={{path/to/directory}} --disable-web-security`

- 打开时为每个标签页自动打开 DevTools 窗口：

`chromium --auto-open-devtools-for-tabs`
