# vf

> VirtualFish 是一个用于管理 Python 虚拟环境的 Fish shell 工具。
> 更多信息：<https://virtualfish.readthedocs.io/en/latest/>.

- 创建一个虚拟环境：

`vf new {{virtualenv_name}}`

- 为特定的 Python 版本创建一个虚拟环境：

`vf new --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- 激活并使用指定的虚拟环境：

`vf activate {{virtualenv_name}}`

- 将当前虚拟环境连接到当前目录，这样每次进入目录时虚拟环境会自动激活（离开时自动停用）：

`vf connect`

- 停用当前虚拟环境：

`vf deactivate`

- 列出所有虚拟环境：

`vf ls`

- 删除一个虚拟环境：

`vf rm {{virtualenv_name}}`

- 显示帮助：

`vf help`
