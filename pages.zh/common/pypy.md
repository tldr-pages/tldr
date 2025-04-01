# pypy

> Python 语言的快速且符合规范的替代实现。
> 更多信息：<https://doc.pypy.org>.

- 启动交互式 shell (REPL)：

`pypy`

- 执行给定 Python 文件中的脚本：

`pypy {{path/to/file.py}}`

- 作为交互式 shell 的一部分执行脚本：

`pypy -i {{path/to/file.py}}`

- 执行 Python 表达式：

`pypy -c "{{expression}}"`

- 以脚本形式运行库模块（终止选项列表）：

`pypy -m {{module}} {{arguments}}`

- 使用 pip 安装包：

`pypy -m pip install {{package}}`

- 交互式调试 Python 脚本：

`pypy -m pdb {{path/to/file.py}}`
