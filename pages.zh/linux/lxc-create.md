# lxc-create

> 创建 Linux 容器。
> 更多信息：<https://linuxcontainers.org/lxc/getting-started>.

- 在 `/var/lib/lxc/` 交互式创建容器：

`sudo lxc-create {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download`

- 在指定目录中创建容器：

`sudo lxc-create {{[-P|--lxcpath]}} {{/path/to/directory/}} {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download`

- 创建容器时传递模板选项：

`sudo lxc-create {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download -- {{[-d|--dist]}} {{distro-name}} {{[-r|--release]}} {{release-version}} {{[-a|--arch]}} {{arch}}`

- 显示帮助：

`lxc-create {{[-?|--help]}}`
