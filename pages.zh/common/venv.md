# venv

> 创建轻量的 Python 虚拟环境。
> 更多信息：<https://docs.python.org/library/venv.html>。

- 创建一个 Python 虚拟环境：

`python -m venv {{路径/到/虚拟环境}}`

- 激活虚拟环境（Linux 和 macOS）：

`{{[.|source]}} {{路径/到/虚拟环境}}/bin/activate`

- 激活虚拟环境（Windows）：

`{{路径\到\虚拟环境}}\Scripts\activate.bat`

- 停用虚拟环境：

`deactivate`

- 创建一个生成 `.venv` 文件夹并自动激活它的别名：

`alias venv='python -m venv .venv && source {{.venv/bin/activate|.venv\Scripts\activate.bat}}'`
