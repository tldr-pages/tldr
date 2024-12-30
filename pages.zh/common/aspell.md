# aspell

> 交互式拼写检查器。
> 更多信息：<http://aspell.net/>.

- 检查单个文件的拼写：

`aspell check {{path/to/file}}`

- 从 `stdin` 列出拼写错误的单词：

`cat {{path/to/file}} | aspell list`

- 显示可用的字典语言：

`aspell dicts`

- 使用不同语言运行 `aspell`（需要两个字母的 ISO 639 语言代码）：

`aspell --lang={{cs}}`

- 从 `stdin` 列出拼写错误的单词，并忽略个人词汇表中的单词：

`cat {{path/to/file}} | aspell --personal={{personal-word-list.pws}} list`