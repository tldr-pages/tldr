# pip

> Python 主流的包安装管理工具。
> 更多信息：<https://pip.pypa.io/>.

- 安装指定包（通过 `pip install` 查看更多示例）：

`pip install {{包名}}`

- 通过依赖文件（如 requirements.txt）来进行安装：

`pip install -r requirements.txt`

- 通过 wheels 文件（扩展名 *.whl）来进行安装：

`pip install {{包名-1.0-py2.py3-none-any.whl}}`

- 升级指定的包：

`pip install --upgrade {{包名}}`

- 卸载指定的包：

`pip uninstall {{包名}}`

- 查看已安装的包：

`pip list`

- 将已安装的包以 Requirements 的格式输出至 requirements.txt 文件中：

`pip freeze > requirements.txt`

- 查看包的详细信息：

`pip show {{包名}}`
