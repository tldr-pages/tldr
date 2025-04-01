# toolbox enter

> 进入一个 `toolbox` 容器进行交互式使用。
> 参见：`toolbox run`。
> 更多信息：<https://manned.org/toolbox-enter.1>。

- 使用特定发行版的默认镜像进入 `toolbox` 容器：

`toolbox enter --distro {{distribution}}`

- 使用当前发行版特定版本的默认镜像进入 `toolbox` 容器：

`toolbox enter --release {{release}}`

- 使用 Fedora 39 的默认镜像进入 toolbox 容器：

`toolbox enter --distro {{fedora}} --release {{f39}}`