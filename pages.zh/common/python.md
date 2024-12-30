# python

> Python 语言解释器。
> 更多信息：<https://www.python.org>。

- 启动 REPL（交互式 shell）：

`python`

- 执行特定的 Python 文件：

`python {{path/to/file.py}}`

- 执行特定的 Python 文件并启动 REPL：

`python -i {{path/to/file.py}}`

- 执行 Python 表达式：

`python -c "{{expression}}"`

- 运行指定库模块的脚本：

`python -m {{module}} {{arguments}}`

- 使用 `pip` 安装包：

`python -m pip install {{package}}`

- 交互式调试 Python 脚本：

`python -m pdb {{path/to/file.py}}`

- 在当前目录启动内置 HTTP 服务器，端口为 8000：

`python -m http.server`