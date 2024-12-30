# ctags

> 为许多流行编程语言的源代码文件中找到的语言对象生成索引（或标签）文件。
> 更多信息：<https://ctags.io/>.

- 为单个文件生成标签，并将其输出到当前目录中名为 "tags" 的文件，如果该文件存在则覆盖：

`ctags {{path/to/file}}`

- 为当前目录中的所有文件生成标签，并将其输出到指定文件，如果该文件存在则覆盖：

`ctags -f {{path/to/file}} *`

- 为当前目录及所有子目录中的所有文件生成标签：

`ctags --recurse`

- 为单个文件生成标签，并以 JSON 格式输出起始行号和结束行号：

`ctags --fields=+ne --output-format=json {{path/to/file}}`