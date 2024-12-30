# mamba

> 快速的跨平台包管理器，旨在作为conda的直接替代品。
> 一些子命令如`repoquery`有自己的使用文档。
> 更多信息：<https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>。

- 创建一个新环境，并在其中安装指定的包：

`mamba create --name {{environment_name}} {{python=3.10 matplotlib}}`

- 在当前环境中安装包，指定包的[c]hannel：

`mamba install -c {{conda-forge}} {{python=3.6 numpy}}`

- 更新当前环境中的所有包：

`mamba update --all`

- 在各个仓库中搜索特定包：

`mamba repoquery search {{numpy}}`

- 列出所有环境：

`mamba info --envs`

- 从缓存中删除未使用的[p]包和[t]arballs：

`mamba clean -pt`

- 激活一个环境：

`mamba activate {{environment_name}}`

- 列出当前激活环境中安装的所有包：

`mamba list`