# lighthouse

> 分析 Web 应用程序和网页，收集现代性能指标和开发最佳实践的见解。
> 更多信息：<https://github.com/GoogleChrome/lighthouse>.

- 为特定网站生成 HTML 报告并保存到当前目录的文件中：

`lighthouse {{https://example.com}}`

- 生成 JSON 报告并打印：

`lighthouse --output {{json}} {{https://example.com}}`

- 生成 JSON 报告并保存到指定文件：

`lighthouse --output {{json}} --output-path {{path/to/file.json}} {{https://example.com}}`

- 使用无头模式生成报告，且不将日志输出到 `stdout`：

`lighthouse --quiet --chrome-flags="{{--headless}}" {{https://example.com}}`

- 生成报告时，使用指定 JSON 文件中的 HTTP 头键值对：

`lighthouse --extra-headers={{path/to/file.json}} {{https://example.com}}`

- 仅生成特定类别的报告：

`lighthouse --only-categories={{performance,accessibility,best-practices,seo,pwa}} {{https://example.com}}`

- 生成报告时启用设备模拟并禁用所有限流：

`lighthouse --screenEmulation.disabled --throttling-method={{provided}} --no-emulatedUserAgent {{https://example.com}}`

- 显示帮助：

`lighthouse --help`