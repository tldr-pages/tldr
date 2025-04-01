# hugo server

> 使用 Hugo 内置的网络服务器构建并提供网站服务。
> 更多信息：<https://gohugo.io/commands/hugo_server/>.

- 构建并提供网站服务：

`hugo server`

- 在指定端口号上构建并提供网站服务：

`hugo server --port {{port_number}}`

- 构建并提供网站服务时压缩支持的输出格式（HTML、XML 等）：

`hugo server --minify`

- 在生产环境中构建并提供网站服务，完全重新渲染并压缩支持的格式：

`hugo server --environment {{production}} --disableFastRender --minify`

- 显示帮助信息：

`hugo server --help`