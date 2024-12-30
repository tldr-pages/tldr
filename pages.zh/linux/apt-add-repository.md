# apt-add-repository

> 管理 `apt` 仓库定义。
> 更多信息：<https://manned.org/apt-add-repository.1>。

- 添加一个新的 `apt` 仓库：

`apt-add-repository {{repository_spec}}`

- 移除一个 `apt` 仓库：

`apt-add-repository --remove {{repository_spec}}`

- 在添加仓库后更新软件包缓存：

`apt-add-repository --update {{repository_spec}}`

- 启用源软件包：

`apt-add-repository --enable-source {{repository_spec}}`