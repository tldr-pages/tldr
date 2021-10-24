# virtualenv

> 创建被隔离的的 Python 虚拟环境。
> 更多信息：<https://virtualenv.pypa.io/>.

- 创建新环境：

`virtualenv {{path/to/venv}}`

- 自定义提示符：

`virtualenv --prompt={{prompt_prefix}} {{path/to/venv}}`

- 为虚拟环境使用不同的 Python 版本：

`virtualenv --python={{path/to/pythonbin}} {{path/to/venv}}`

- 启动（选择）环境：

`source {{path/to/venv}}/bin/activate`

- 停止环境：

`deactivate`
