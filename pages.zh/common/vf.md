# vf

> VirtualFish 是一个用于管理 Python 虚拟环境的 fish shell 工具。
> 更多信息请访问：<https://virtualfish.readthedocs.io/en/latest/>。

- 创建一个虚拟环境：

`vf new {{virtualenv_name}}`

- 为特定的 Python 版本创建一个虚拟环境：

`vf new --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- 激活并使用指定的虚拟环境：

`vf activate {{virtualenv_name}}`

- 将当前虚拟环境连接到当前目录，以便在您进入该目录时自动激活（在您离开时自动停用）：

`vf connect`

- 停用当前虚拟环境：

`vf deactivate`

- 列出所有虚拟环境：

`vf ls`

- 删除一个虚拟环境：

`vf rm {{virtualenv_name}}`

- 显示帮助信息：

`vf help`