# add-apt-repository

> 管理 `apt` 仓库定义。
> 更多信息：<https://manned.org/apt-add-repository>。

- 添加一个新的 `apt` 仓库：

`add-apt-repository {{repository_spec}}`

- 移除一个 `apt` 仓库：

`add-apt-repository --remove {{repository_spec}}`

- 在添加仓库后更新软件包缓存：

`add-apt-repository --update {{repository_spec}}`

- 允许从仓库下载源软件包：

`add-apt-repository --enable-source {{repository_spec}}`