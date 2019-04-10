# aspell

> 交互式拼写检查工具.

- 为一个文件做拼写检查:

`aspell check {{文件路径}}`

- 列出来自标准输入的拼写错误单词:

`cat {{文件}} | aspell list`

- 列出可用的字典语言:

`aspell dicts`

- 指定不同的语言(取ISO 639语言代码的2个字母)来运行aspell:

`aspell --lang={{cs}}`

- 列出来自标准输入的拼写错误单词，并且忽略个人单词列表中的单词:

`cat {{文件}} | aspell --personal={{个人单词列表.pws}} {{列表}}`
