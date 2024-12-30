# hugo 服务器

> 使用 Hugo 内置的网页服务器构建和提供网站。
> 更多信息：<https://gohugo.io/commands/hugo_server/>.

- 构建并提供一个网站：

`hugo server`

- 在指定的端口号上构建并提供一个网站：

`hugo server --port {{port_number}}`

- 在构建和提供网站时压缩支持的输出格式（HTML、XML等）：

`hugo server --minify`

- 在生产环境中构建并提供一个网站，进行完全重渲染，并压缩支持的格式：

`hugo server --environment {{production}} --disableFastRender --minify`

- 显示帮助信息：

`hugo server --help`