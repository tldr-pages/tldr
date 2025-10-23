# conda

> 为任何编程语言准备的包、依赖和环境管理工具。
> 部分子命令（例如 `create`）有自己的文档。
> 更多信息：<https://docs.conda.io/projects/conda/en/latest/commands/index.html>.

- 创建新的环境，并将指定包安装入该环境：

`conda create {{[-n|--name]}} {{环境_名称}} {{python=3.9 matplotlib}}`

- 列出所有环境：

`conda info {{[-e|--envs]}}`

- 激活某个环境：

`conda activate {{环境_名称}}`

- 取消激活某个环境：

`conda deactivate`

- 删除一个环境（会移除所有的包）：

`conda remove {{[-n|--name]}} {{环境_名称}} --all`

- 将多个包按照到当前环境：

`conda install {{python=3.4 numpy}}`

- 列出当前环境中的已安装包：

`conda list`

- 删除未使用的包和缓存：

`conda clean {{[-a|--all]}}`
