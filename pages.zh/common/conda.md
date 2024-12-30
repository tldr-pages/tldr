# conda

> 适用于任何编程语言的包、依赖和环境管理。
> 一些子命令如 `create` 有其自己的使用文档。
> 更多信息：<https://github.com/conda/conda>。

- 创建一个新环境，并在其中安装指定的包：

`conda create --name {{environment_name}} {{python=3.9 matplotlib}}`

- 列出所有环境：

`conda info --envs`

- 加载一个环境：

`conda activate {{environment_name}}`

- 卸载一个环境：

`conda deactivate`

- 删除一个环境（移除所有包）：

`conda remove --name {{environment_name}} --all`

- 在当前环境中安装包：

`conda install {{python=3.4 numpy}}`

- 列出当前环境中安装的包：

`conda list`

- 删除未使用的包和缓存：

`conda clean --all`