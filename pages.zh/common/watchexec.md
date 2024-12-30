# watchexec

> 当文件更改时运行任意命令。
> 更多信息：<https://github.com/watchexec/watchexec>。

- 当当前目录中的任何文件更改时，调用 `ls -la`：

`watchexec {{ls -la}}`

- 当当前目录中的任何 JavaScript、CSS 和 HTML 文件更改时，运行 `make`：

`watchexec --exts {{js,css,html}} make`

- 当 `lib` 或 `src` 目录中的任何文件更改时，运行 `make`：

`watchexec --watch {{lib}} --watch {{src}} {{make}}`

- 当当前目录中的任何文件更改时，调用/重启 `my_server`，发送 `SIGKILL` 以停止子进程：

`watchexec --restart --stop-signal {{SIGKILL}} {{my_server}}`