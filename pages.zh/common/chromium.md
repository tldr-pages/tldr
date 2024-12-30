# chromium

> 由谷歌主要开发和维护的开源网页浏览器。
> 注意：您可能需要将 `chromium` 命令替换为您想要的网页浏览器，例如 `brave`、`google-chrome`、`opera` 或 `vivaldi`。
> 更多信息：<https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- 打开特定的 URL 或文件：

`chromium {{https://example.com|path/to/file.html}}`

- 以隐身模式打开：

`chromium --incognito {{example.com}}`

- 在新窗口中打开：

`chromium --new-window {{example.com}}`

- 以应用模式打开（没有工具栏、URL 地址栏、按钮等）：

`chromium --app={{https://example.com}}`

- 使用代理服务器：

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 使用自定义的配置文件目录打开：

`chromium --user-data-dir={{path/to/directory}}`

- 在不进行 CORS 验证的情况下打开（适合测试 API）：

`chromium --user-data-dir={{path/to/directory}} --disable-web-security`

- 为每个打开的标签页打开 DevTools 窗口：

`chromium --auto-open-devtools-for-tabs`