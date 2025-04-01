# pipwin

> 一个用于在 Windows 上安装非官方 Python 包二进制文件的工具。
> 更多信息：<https://github.com/lepisma/pipwin>.

- 列出所有可下载的包：

`pipwin list`

- 搜索包：

`pipwin search {{partial_name|name}}`

- 安装包：

`pipwin install {{package}}`

- 卸载包：

`pipwin uninstall {{package}}`

- 将包下载到特定目录：

`pipwin download --dest {{path\to\directory}} {{package}}`

- 根据 `requirements.txt` 安装包：

`pipwin install --file {{path\to\requirements.txt}}`