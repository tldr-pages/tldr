# pypy

> 快速且符合规范的Python语言替代实现。
> 更多信息：<https://doc.pypy.org>。

- 启动REPL（交互式命令行）：

`pypy`

- 执行指定Python文件中的脚本：

`pypy {{path/to/file.py}}`

- 作为交互式命令行的一部分执行脚本：

`pypy -i {{path/to/file.py}}`

- 执行Python表达式：

`pypy -c "{{expression}}"`

- 将库模块作为脚本运行（终止选项列表）：

`pypy -m {{module}} {{arguments}}`

- 使用pip安装包：

`pypy -m pip install {{package}}`

- 互动调试Python脚本：

`pypy -m pdb {{path/to/file.py}}`