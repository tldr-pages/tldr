# fastmod

> 这是一个快速的部分替代codemod工具，用于在整个代码库中替换和全部替换。
> 正则表达式由Rust的regex库进行匹配。
> 更多信息：<https://github.com/facebookincubator/fastmod>。

- 在当前目录的所有文件中替换正则表达式模式，忽略在.ignore和.gitignore中的文件：

`fastmod {{regex_pattern}} {{replacement}}`

- 在特定文件或目录中以不区分大小写的模式替换正则表达式模式：

`fastmod --ignore-case {{regex_pattern}} {{replacement}} -- {{path/to/file path/to/directory ...}}`

- 在特定目录中使用不区分大小写的glob模式过滤的文件中替换正则表达式模式：

`fastmod {{regex}} {{replacement}} --dir {{path/to/directory}} --iglob {{'**/*.{js,json}'}}`

- 在`.js`或JSON文件中替换确切字符串：

`fastmod --fixed-strings {{exact_string}} {{replacement}} --extensions {{json,js}}`

- 在没有确认提示的情况下替换确切字符串（禁用正则表达式）：

`fastmod --accept-all --fixed-strings {{exact_string}} {{replacement}}`

- 在没有确认提示的情况下替换确切字符串，并打印更改的文件：

`fastmod --accept-all --print-changed-files --fixed-strings {{exact_string}} {{replacement}}`