# ctags

> 为多种流行编程语言的源文件中找到的语言对象生成索引（或标签）文件。
> 更多信息：<https://ctags.io/>.

- 为单个文件生成标签，并输出到当前目录下的名为 "tags" 的文件中，如果文件存在则覆盖：

`ctags {{path/to/file}}`

- 为当前目录下的所有文件生成标签，并输出到指定文件中，如果文件存在则覆盖：

`ctags -f {{path/to/file}} *`

- 为当前目录及其所有子目录中的所有文件生成标签：

`ctags --recurse`

- 为单个文件生成标签，并以 JSON 格式输出包含开始行号和结束行号：

`ctags --fields=+ne --output-format=json {{path/to/file}}`