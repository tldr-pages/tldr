# nokogiri

> 一个HTML、XML、SAX和Reader解析器。
> 更多信息：<https://nokogiri.org>。

- 解析URL或文件的内容：

`nokogiri {{url|path/to/file}}`

- 作为特定类型解析：

`nokogiri {{url|path/to/file}} --type {{xml|html}}`

- 在解析前加载特定的初始化文件：

`nokogiri {{url|path/to/file}} -C {{path/to/config_file}}`

- 使用特定编码解析：

`nokogiri {{url|path/to/file}} --encoding {{encoding}}`

- 使用RELAX NG文件验证：

`nokogiri {{url|path/to/file}} --rng {{url|path/to/file}}`
