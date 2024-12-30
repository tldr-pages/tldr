# phpcs

> 对 PHP、JavaScript 和 CSS 文件进行分词，以检测是否违反已定义的编码标准。
> 更多信息：<https://github.com/squizlabs/PHP_CodeSniffer>。

- 检查指定目录中的问题（默认为 PEAR 标准）：

`phpcs {{path/to/directory}}`

- 显示已安装的编码标准列表：

`phpcs -i`

- 指定要验证的编码标准：

`phpcs {{path/to/directory}} --standard {{standard}}`

- 指定在检查时包含的文件扩展名，以逗号分隔：

`phpcs {{path/to/directory}} --extensions {{file_extension1,file_extension2,...}}`

- 指定输出报告的格式（例如 `full`、`xml`、`json`、`summary`）：

`phpcs {{path/to/directory}} --report {{format}}`

- 设置在处理过程中使用的配置变量：

`phpcs {{path/to/directory}} --config-set {{key}} {{value}}`

- 在处理之前加载的文件的逗号分隔列表：

`phpcs {{path/to/directory}} --bootstrap {{path/to/file1,path/to/file2,...}}`

- 不递归进入子目录：

`phpcs {{path/to/directory}} -l`