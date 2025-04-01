# sd

> 直观的查找和替换工具。
> 更多信息：<https://github.com/chmln/sd>.

- 使用正则表达式修剪一些空白（输出流：`stdout`）：

`{{echo 'lorem ipsum 23   '}} | sd '\s+$' ''`

- 使用捕获组替换单词（输出流：`stdout`）：

`{{echo 'cargo +nightly watch'}} | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- 在特定文件中查找和替换（输出流：`stdout`）：

`sd -p {{'window.fetch'}} {{'fetch'}} {{path/to/file.js}}`

- 在当前项目的所有文件中查找和替换（输出流：`stdout`）：

`sd {{'from "react"'}} {{'from "preact"'}} "$(find . -type f)"`
