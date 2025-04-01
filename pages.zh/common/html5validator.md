# html5validator

> 验证 HTML5。
> 更多信息：<https://github.com/svenkreiss/html5validator>。

- 验证特定文件：

`html5validator {{path/to/file}}`

- 验证特定目录中的所有 HTML 文件：

`html5validator --root {{path/to/directory}}`

- 显示警告和错误：

`html5validator --show-warnings {{path/to/file}}`

- 使用通配符匹配多个文件：

`html5validator --root {{path/to/directory}} --match "{{*.html *.php}}"`

- 忽略特定目录名称：

`html5validator --root {{path/to/directory}} --blacklist "{{node_modules vendor}}"`

- 以特定格式输出结果：

`html5validator --format {{gnu|xml|json|text}} {{path/to/file}}`

- 以特定详细程度输出日志：

`html5validator --root {{path/to/directory}} --log {{debug|info|warning}}`