# fastmod

> 一个快速部分替代 codemod 工具，用于在整个代码库中替换和替换所有。
> 正则表达式由 Rust 正则表达式库匹配。
> 更多信息：<https://github.com/facebookincubator/fastmod>.

- 替换当前目录中所有文件中的正则表达式模式，忽略 .ignore 和 .gitignore 文件中的文件：

`fastmod {{regex_pattern}} {{replacement}}`

- 以不区分大小写的方式替换特定文件或目录中的正则表达式模式：

`fastmod --ignore-case {{regex_pattern}} {{replacement}} -- {{path/to/file path/to/directory ...}}`

- 在特定目录中以不区分大小写的 glob 模式过滤的文件中替换正则表达式模式：

`fastmod {{regex}} {{replacement}} --dir {{path/to/directory}} --iglob {{'**/*.{js,json}'}}`

- 替换 .js 或 JSON 文件中的确切字符串：

`fastmod --fixed-strings {{exact_string}} {{replacement}} --extensions {{json,js}}`

- 替换确切字符串而不提示确认（禁用正则表达式）：

`fastmod --accept-all --fixed-strings {{exact_string}} {{replacement}}`

- 替换确切字符串而不提示确认，并打印更改的文件：

`fastmod --accept-all --print-changed-files --fixed-strings {{exact_string}} {{replacement}}`
