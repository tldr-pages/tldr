# pageres

> 捕获网站在不同分辨率下的屏幕截图。
> 更多信息：<https://github.com/sindresorhus/pageres-cli>.

- 为多个 URL 在不同分辨率下捕获多个屏幕截图：

`pageres {{https://example.com/}} {{https://example2.com/}} {{1366x768}} {{1600x900}}`

- 为某个 URL 提供特定选项，覆盖全局选项：

`pageres [{{https://example.com/}} {{1366x768}} --no-crop] [{{https://example2.com/}} {{1024x768}}] --crop`

- 提供自定义文件名模板：

`pageres {{https://example.com/}} {{1024x768}} --filename={{'<%= date %> - <%= url %>'}}`

- 捕获页面上的特定元素：

`pageres {{https://example.com/}} {{1366x768}} --selector='{{.page-header}}'`

- 隐藏特定元素：

`pageres {{https://example.com/}} {{1366x768}} --hide='{{.page-header}}'`

- 捕获本地文件的屏幕截图：

`pageres {{local_file_path.html}} {{1366x768}}`
