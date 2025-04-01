# go list

> 列出包或模块。
> 更多信息：<https://golang.org/cmd/go/#hdr-List_packages_or_modules>。

- 列出包：

`go list ./...`

- 列出标准库包：

`go list std`

- 以 JSON 格式列出包：

`go list -json time net/http`

- 列出模块依赖及其可用更新：

`go list -m -u all`
