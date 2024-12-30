# nokogiri

> 一款 HTML、XML、SAX 和 Reader 解析器。
> 更多信息：<https://nokogiri.org>。

- 解析 URL 或文件的内容：

`nokogiri {{url|path/to/file}}`

- 作为特定类型解析：

`nokogiri {{url|path/to/file}} --type {{xml|html}}`

- 在解析之前加载特定的初始化文件：

`nokogiri {{url|path/to/file}} -C {{path/to/config_file}}`

- 使用特定编码进行解析：

`nokogiri {{url|path/to/file}} --encoding {{encoding}}`

- 使用 RELAX NG 文件进行验证：

`nokogiri {{url|path/to/file}} --rng {{url|path/to/file}}`