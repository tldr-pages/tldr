# pip3

> Python 包管理器。
> 更多信息：<https://pip.pypa.io>。

- 安装一个包：

`pip3 install {{package}}`

- 安装特定版本的包：

`pip3 install {{package}}=={{version}}`

- 升级一个包：

`pip3 install --upgrade {{package}}`

- 卸载一个包：

`pip3 uninstall {{package}}`

- 将已安装的包列表保存到文件：

`pip3 freeze > {{requirements.txt}}`

- 从文件中安装包：

`pip3 install --requirement {{requirements.txt}}`

- 显示已安装包的信息：

`pip3 show {{package}}`
