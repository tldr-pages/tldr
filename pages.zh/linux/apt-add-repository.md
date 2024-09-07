# apt-add-repository

> 管理 APT 仓库。
> 更多信息：<https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- 添加一个 APT 仓库：

`apt-add-repository {{repository_spec}}`

- 移除一个 APT 仓库：

`apt-add-repository --remove {{repository_spec}}`

- 添加一个 APT 仓库之后更新包缓存：

`apt-add-repository --update {{repository_spec}}`

- 开启源码包：

`apt-add-repository --enable-source {{repository_spec}}`
