# mamba repoquery

> 高效查询 conda 和 mamba 包仓库及包依赖关系。
> 更多信息：<https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>。

- 搜索特定包的所有可用版本：

`mamba repoquery search {{package}}`

- 搜索满足特定约束的所有包：

`mamba repoquery search {{sphinx<5}}`

- 以树形格式列出当前激活环境中已安装包的依赖：

`mamba repoquery depends --tree {{scipy}}`

- 打印当前环境中需要安装特定包的包（即 `depends` 的反向查询）：

`mamba repoquery whoneeds {{ipython}}`