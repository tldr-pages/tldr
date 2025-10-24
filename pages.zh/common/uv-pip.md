# uv pip

> 提供类似 pip 的命令，用于安装、卸载和管理程序包。
> 更多信息：<https://docs.astral.sh/uv/reference/cli/#uv-pip>.

- 安装一个包：

`uv pip install {{包名}}`

- 根据程序包依赖需求文件，安装程序包：

`uv pip install {{[-r|--requirements]}} {{requirements.txt}}`

- 安装特定版本的一个包：

`uv pip install {{包名==1.2.3}}`

- 卸载一个包

`uv pip uninstall {{包名}}`

- 将安装的包列表，保存到文件：

`uv pip freeze > {{requirements.txt}}`

- 列出安装的包：

`uv pip list`

- 展示关于某个已安装包的信息：

`uv pip show {{包名}}`

- 将环境与程序包依赖需求文件进行同步（将会安装/卸载程序包，来完全匹配该文件）：

`uv pip sync {{requirements.txt}}`
