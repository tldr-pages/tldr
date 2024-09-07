# chromium

> 主要由 Google 开发和维护的开源网络浏览器。
> 更多信息：<https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- 打开指定 URL 或文件：

`chromium {{https://example.com}}|路径/到/文件.html`

- 以隐身模式打开：

`chromium --incognito {{example.com}}`

- 在新窗口打开：

`chromium --new-window {{example.com}}`

- 以应用模式打开（没有工具栏、URL 栏、按钮等）：

`chromium --app={{https://example.com}}`

- 使用代理服务器：

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- 使用自定义配置目录打开：

`chromium --user-data-dir={{路径/到/目录}}`

- 无需 CORS 验证即可打开（用于测试 API）：

`chromium --user-data-dir={{路径/到/目录}} --disable-web-security`

- 每个打开的选项卡都会打开一个 DevTools 窗口：

`chromium --auto-open-devtools-for-tabs`
