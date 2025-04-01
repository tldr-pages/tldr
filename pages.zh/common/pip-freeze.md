# pip freeze

> 以需求格式列出已安装的包。
> 更多信息：<https://pip.pypa.io/en/stable/cli/pip_freeze>。

- 列出已安装的包：

`pip freeze`

- 列出已安装的包并写入 `requirements.txt` 文件：

`pip freeze > requirements.txt`

- 列出虚拟环境中的已安装包，排除全局安装的包：

`pip freeze --local > requirements.txt`

- 列出用户站点中的已安装包：

`pip freeze --user > requirements.txt`

- 列出所有包，包括 `pip`、`distribute`、`setuptools` 和 `wheel`（默认情况下这些包会被跳过）：

`pip freeze --all > requirements.txt`