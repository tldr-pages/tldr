# mamba repoquery

> 高效查询 conda 和 mamba 包仓库及包依赖。
> 更多信息：<https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>。

- 搜索特定包的所有可用版本：

`mamba repoquery search {{package}}`

- 搜索满足特定约束条件的所有包：

`mamba repoquery search {{sphinx<5}}`

- 以树状格式列出当前激活环境中安装的包的依赖项：

`mamba repoquery depends --tree {{scipy}}`

- 打印当前环境中依赖特定包的包（即 `depends` 的反向操作）：

`mamba repoquery whoneeds {{ipython}}`
