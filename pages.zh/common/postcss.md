# postcss

> 使用 JS 插件转换样式。
> 更多信息：<https://postcss.org>。

- 解析和转换 CSS 文件：

`postcss {{path/to/file}}`

- 解析和转换 CSS 文件，并输出到指定文件：

`postcss {{path/to/file}} --output {{path/to/file}}`

- 解析和转换 CSS 文件，并输出到指定目录：

`postcss {{path/to/file}} --dir {{path/to/directory}}`

- 解析和转换 CSS 文件，并就地更新：

`postcss {{path/to/file}} --replace`

- 指定自定义的 PostCSS 解析器：

`postcss {{path/to/file}} --parser {{parser}}`

- 指定自定义的 PostCSS 语法：

`postcss {{path/to/file}} --syntax {{syntax}}`

- 监视 CSS 文件的变化：

`postcss {{path/to/file}} --watch`

- 显示帮助信息：

`postcss --help`