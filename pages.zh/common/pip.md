# pip

> Python 包管理器。
> 一些子命令如 `install` 有自己的使用文档。
> 更多信息：<https://pip.pypa.io>。

- 安装一个包（请参见 `pip install` 以获取更多安装示例）：

`pip install {{package}}`

- 将包安装到用户目录，而不是系统默认位置：

`pip install --user {{package}}`

- 升级一个包：

`pip install --upgrade {{package}}`

- 卸载一个包：

`pip uninstall {{package}}`

- 将已安装的包保存到文件：

`pip freeze > {{requirements.txt}}`

- 显示已安装包的信息：

`pip show {{package}}`

- 从文件安装包：

`pip install --requirement {{requirements.txt}}`