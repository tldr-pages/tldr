# lighthouse

> 分析 web 应用程序和网页，收集现代性能指标和开发者最佳实践的见解。
> 更多信息：<https://github.com/GoogleChrome/lighthouse>。

- 为特定网站生成 HTML 报告并将其保存到当前目录的文件中：

`lighthouse {{https://example.com}}`

- 生成 JSON 报告并打印出来：

`lighthouse --output {{json}} {{https://example.com}}`

- 生成 JSON 报告并将其保存到特定文件：

`lighthouse --output {{json}} --output-path {{path/to/file.json}} {{https://example.com}}`

- 使用无头模式的浏览器生成报告，不记录到 `stdout`：

`lighthouse --quiet --chrome-flags="{{--headless}}" {{https://example.com}}`

- 使用指定 JSON 文件中的 HTTP 头键/值对为所有请求生成报告：

`lighthouse --extra-headers={{path/to/file.json}} {{https://example.com}}`

- 仅为特定类别生成报告：

`lighthouse --only-categories={{performance,accessibility,best-practices,seo,pwa}} {{https://example.com}}`

- 生成一个禁用设备仿真和所有限速的报告：

`lighthouse --screenEmulation.disabled --throttling-method={{provided}} --no-emulatedUserAgent {{https://example.com}}`

- 显示帮助信息：

`lighthouse --help`