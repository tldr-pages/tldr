# cat

> 打印和连接文件。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- 将文件内容打印到 `stdout`：

`cat {{路径/到/文件}}`

- 将多个文件连接到一个输出文件：

`cat {{路径/到/文件1 路径/到/文件2 ...}} > {{路径/到/输出文件}}`

- 将多个文件附加到输出文件：

`cat {{路径/到/文件1 路径/到/文件2 ...}} >> {{路径/到/输出文件}}`

- 将 `stdin` 写入文件：

`cat - > {{路径/到/文件}}`

- 显示带有行号的所有行：

`cat {{[-n|--number]}} {{路径/到/文件}}`

- 显示不可打印字符和空白字符（如果非 ASCII，则带有 `M-` 前缀）：

`cat {{[-vte|--show-nonprinting -t -e]}} {{路径/到/文件}}`
