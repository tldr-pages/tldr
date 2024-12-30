# pip 安装

> 安装 Python 包。
> 更多信息请访问：<https://pip.pypa.io>。

- 安装一个包：

`pip install {{package}}`

- 安装特定版本的包：

`pip install {{package}}=={{version}}`

- 安装文件中列出的包：

`pip install -r {{path/to/requirements.txt}}`

- 从 URL 或本地文件归档(.tar.gz | .whl)安装包：

`pip install --find-links {{url|path/to/file}}`

- 以开发（可编辑）模式安装当前目录中的本地包：

`pip install --editable {{.}}`