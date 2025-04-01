# tldr-lint

> 检查和格式化 `tldr` 页面。
> 更多信息：<https://github.com/tldr-pages/tldr-lint>.

- 检查所有页面：

`tldr-lint {{pages_directory}}`

- 将特定页面格式化输出到 `stdout`：

`tldr-lint --format {{page.md}}`

- 在原地格式化所有页面：

`tldr-lint --format --in-place {{pages_directory}}`