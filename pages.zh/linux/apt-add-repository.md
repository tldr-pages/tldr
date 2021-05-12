# apt-add-repository

> 管理 apt 仓库。

- 添加一个 apt 仓库：

`apt-add-repository {{repository_spec}}`

- 移除一个 apt 仓库：

`apt-add-repository --remove {{repository_spec}}`

- 添加一个 apt 仓库之后更新包缓存：

`apt-add-repository --update {{repository_spec}}`

- 开启源码包：

`apt-add-repository --enable-source {{repository_spec}}`
