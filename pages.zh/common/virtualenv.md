# virtualenv

> 创建虚拟隔离的 Python 环境。
> 更多信息：<https://virtualenv.pypa.io/>。

- 创建一个新的环境：

`virtualenv {{path/to/venv}}`

- 自定义提示前缀：

`virtualenv --prompt={{prompt_prefix}} {{path/to/venv}}`

- 使用不同版本的 Python 创建虚拟环境：

`virtualenv --python={{path/to/pythonbin}} {{path/to/venv}}`

- 启动（选择）环境：

`source {{path/to/venv}}/bin/activate`

- 停止环境：

`deactivate`