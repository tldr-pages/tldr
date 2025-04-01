# highlight

> 输出带有语法高亮的源代码，支持多种格式。
> 更多信息：<http://www.andre-simon.de/doku/highlight/highlight.php>。

- 从源代码文件生成完整的 HTML 文档：

`highlight --out-format={{html}} --style {{theme_name}} --syntax {{language}} {{path/to/source_code}}`

- 生成适合嵌入到更大文档中的 HTML 片段：

`highlight --out-format={{html}} --fragment --syntax {{language}} {{source_file}}`

- 在每个标签中内联 CSS 样式：

`highlight --out-format={{html}} --inline-css --syntax {{language}} {{source_file}}`

- 列出所有支持的语言、主题或插件：

`highlight --list-scripts {{langs|themes|plugins}}`

- 打印某个主题的 CSS 样式表：

`highlight --out-format={{html}} --print-style --style {{theme_name}} --syntax {{language}} --stdout`
