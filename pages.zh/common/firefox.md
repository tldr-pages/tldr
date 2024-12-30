# firefox

> 一个免费和开源的网页浏览器。
> 更多信息：<https://developer.mozilla.org/zh-CN/docs/Mozilla/Command_Line_Options>。

- 启动 Firefox 并打开一个网页：

`firefox {{https://www.duckduckgo.com}}`

- 打开一个新窗口：

`firefox --new-window {{https://www.duckduckgo.com}}`

- 打开一个私人（隐身）窗口：

`firefox --private-window`

- 使用默认搜索引擎搜索“维基百科”：

`firefox --search "{{维基百科}}"`

- 在安全模式下启动 Firefox，禁用所有扩展：

`firefox --safe-mode`

- 在无头模式下截取网页的屏幕截图：

`firefox --headless --screenshot {{path/to/output_file.png}} {{https://example.com/}}`

- 使用特定配置文件允许同时运行多个独立的 Firefox 实例：

`firefox --profile {{path/to/directory}} {{https://example.com/}}`

- 将 Firefox 设置为默认浏览器：

`firefox --setDefaultBrowser`