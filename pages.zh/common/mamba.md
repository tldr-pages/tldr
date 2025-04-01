# mamba

> 快速、跨平台的包管理器，旨在作为 conda 的直接替代品。
> 某些子命令（如 `repoquery`）有自己的使用文档。
> 更多信息：<https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- 创建一个新环境，并在其中安装指定的包：

`mamba create {{[-n|--name]}} {{environment_name}} {{python=3.10 matplotlib}}`

- 在当前环境中安装包，并指定包的频道：

`mamba install {{[-c|--channel]}} {{conda-forge}} {{python=3.6 numpy}}`

- 更新当前环境中的所有包：

`mamba update --all`

- 跨仓库搜索特定的包：

`mamba repoquery search {{numpy}}`

- 列出所有环境：

`mamba info --envs`

- 从缓存中删除未使用的包和 tarball：

`mamba clean -pt`

- 激活一个环境：

`mamba activate {{environment_name}}`

- 列出当前激活环境中的所有已安装包：

`mamba list`
