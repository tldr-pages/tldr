# tr

> 转换字符：基于单个字符和字符集执行替换。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- 替换文件中所有出现的某个字符，并打印结果：

`tr {{find_character}} {{replace_character}} < {{path/to/file}}`

- 替换另一个命令输出中所有出现的某个字符：

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- 将第一个集合中的每个字符映射到第二个集合中的相应字符：

`tr '{{abcd}}' '{{jkmn}}' < {{path/to/file}}`

- 从输入中删除指定字符集的所有出现：

`tr {{[-d|--delete]}} '{{input_characters}}' < {{path/to/file}}`

- 将一系列相同的字符压缩为一个字符：

`tr {{[-s|--squeeze-repeats]}} '{{input_characters}}' < {{path/to/file}}`

- 将文件内容转换为大写：

`tr "[:lower:]" "[:upper:]" < {{path/to/file}}`

- 从文件中删除非打印字符：

`tr {{[-cd|--complement --delete]}} "[:print:]" < {{path/to/file}}`