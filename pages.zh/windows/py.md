# py

> 用于 Windows 的 Python 启动器，可运行指定的 Python 版本。
> 另见： `python`.
> 更多信息：<https://docs.python.org/using/windows.html#python-launcher-for-windows>.

- 启动一个 REPL（交互式命令行），可以选择使用 `python` 支持的参数（如 `-c`、`-m` 等）：

`py {{python 参数}}`

- 执行指定的 Python 文件：

`py {{路径/到/文件.py}}`

- 运行指定版本的 Python. 若缺少该版本且设置了 `PYLAUNCHER_ALLOW_INSTALL` 环境变量，则通过 Microsoft Store 或 Winget 自动安装：

`py {{-2|-3.7|...}}`

- 列出已安装的 Python 版本：

`py --list`
