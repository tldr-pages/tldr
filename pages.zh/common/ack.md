# ack

> 一个类似 grep 的搜索工具，为程序员优化。
> 另见 `rg`，它要快得多。
> 更多信息：<https://beyondgrep.com/documentation>.

- 在当前目录下递归地搜索包含一个字符串或正则表达式的文件：

`ack "{{search_pattern}}"`

- 不区分大小写搜索：

`ack {{[-i|--ignore-case]}} "{{search_pattern}}"`

- 搜索匹配模式的行，只打印匹配的文本，而不打印行的其他部分：

`ack {{[-o|--output '$&']}} "{{search_pattern}}"`

- 限制搜索特定类型的文件：

`ack {{[-t|--type]}} {{ruby}} "{{search_pattern}}"`

- 不在特定类型的文件中搜索：

`ack {{[-t|--type]}} no{{ruby}} "{{search_pattern}}"`

- 计算找到的匹配文件的总数：

`ack {{[-c|--count]}} {{[-h|--no-filename]}} "{{search_pattern}}"`

- 只打印文件名和每个文件的匹配数：

`ack {{[-c|--count]}} {{[-l|--files-with-matches]}} "{{search_pattern}}"`

- 列出所有可与 `--type` 一起使用的值：

`ack --help-types`
