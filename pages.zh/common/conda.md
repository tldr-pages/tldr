# conda

> 用于任何编程语言的包、依赖项和环境管理工具。
> 某些子命令（如 `create`）有自己的使用文档。
> 更多信息：<https://github.com/conda/conda>。

- 创建一个新环境，并安装指定的包：

`conda create --name {{environment_name}} {{python=3.9 matplotlib}}`

- 列出所有环境：

`conda info --envs`

- 加载环境：

`conda activate {{environment_name}}`

- 卸载环境：

`conda deactivate`

- 删除环境（移除所有包）：

`conda remove --name {{environment_name}} --all`

- 安装包到当前环境：

`conda install {{python=3.4 numpy}}`

- 列出当前环境中的已安装包：

`conda list`

- 删除未使用的包和缓存：

`conda clean --all`