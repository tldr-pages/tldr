# toolbox create

> 创建新的 `toolbox` 容器。
> 更多信息：<https://manned.org/toolbox-create.1>.

- 为特定发行版创建 `toolbox` 容器：

`toolbox create --distro {{distribution}}`

- 为当前发行版的特定版本创建 `toolbox` 容器：

`toolbox create --release {{release}}`

- 使用自定义镜像创建 `toolbox` 容器：

`toolbox create --image {{name}}`

- 从自定义的 Fedora 镜像创建 `toolbox` 容器：

`toolbox create --image {{registry.fedoraproject.org/fedora-toolbox:39}}`

- 使用 Fedora 39 的默认镜像创建 `toolbox` 容器：

`toolbox create --distro {{fedora}} --release {{f39}}`
