# marimo

> 一个响应式的 Python 笔记本环境。
> 结合了 Jupyter、Streamlit 和其他笔记本工具的特性，并支持响应式执行。
> 更多信息：<https://docs.marimo.io/cli>。

- 通过启动 marimo 服务器来创建或编辑笔记本：

`marimo edit`

- 在特定端口上启动 marimo 服务器且不启动浏览器：

`marimo edit {{[-p|--port]}} {{port_number}} --headless`

- 编辑特定的笔记本：

`marimo edit {{path/to/notebook.py}}`

- 以只读模式作为应用运行 marimo 笔记本：

`marimo run {{path/to/notebook.py}}`

- 开始一个交互式教程来学习 marimo：

`marimo tutorial {{intro|components|dataflow|io}}`

- 查看特定命令的帮助：

`marimo {{edit|run|tutorial|config|new|...}} --help`
