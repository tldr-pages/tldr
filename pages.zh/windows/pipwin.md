# pipwin

> 一种在 Windows 上安装非官方 Python 包二进制文件的工具。
> 更多信息：<https://github.com/lepisma/pipwin>。

- 列出所有可下载的包：

`pipwin list`

- 搜索包：

`pipwin search {{部分名称|名称}}`

- 安装一个包：

`pipwin install {{包}}`

- 卸载一个包：

`pipwin uninstall {{包}}`

- 将一个包下载到指定目录：

`pipwin download --dest {{路径\到\目录}} {{包}}`

- 根据 `requirements.txt` 安装包：

`pipwin install --file {{路径\到\requirements.txt}}`