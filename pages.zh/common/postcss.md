# postcss

> 使用 JS 插件转换样式。
> 更多信息：<https://postcss.org>。

- 解析并转换 CSS 文件：

`postcss {{path/to/file}}`

- 解析并转换 CSS 文件并输出到特定文件：

`postcss {{path/to/file}} --output {{path/to/file}}`

- 解析并转换 CSS 文件并输出到特定目录：

`postcss {{path/to/file}} --dir {{path/to/directory}}`

- 就地解析并转换 CSS 文件：

`postcss {{path/to/file}} --replace`

- 指定自定义 PostCSS 解析器：

`postcss {{path/to/file}} --parser {{parser}}`

- 指定自定义 PostCSS 语法：

`postcss {{path/to/file}} --syntax {{syntax}}`

- 监视 CSS 文件的更改：

`postcss {{path/to/file}} --watch`

- 显示帮助：

`postcss --help`