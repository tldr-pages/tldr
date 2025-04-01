# pct

> 管理 Proxmox 中的 LXC 容器。
> 更多信息：<https://pve.proxmox.com/pve-docs/pct.1.html>.

- 列出所有容器：

`pct list`

- 启动/停止/重启特定容器：

`pct {{start|stop|reboot}} {{100}}`

- 访问特定容器的 shell：

`pct enter {{100}}`

- 从模板创建容器：

`pct create {{100}} {{/var/lib/vz/template/cache/distro-name.tar.zst}} -hostname {{hostname}} -password {{password}} --rootfs {{local-lvm}} --on-boot`

- 将容器的磁盘大小调整为 20G：

`pct resize {{100}} {{rootfs|mpX}} {{20G}}`

- 显示容器的配置，指定其 ID：

`pct config {{100}}`

- 为特定容器创建快照，附带描述：

`pct snapshot {{100}} {{my-snapshot}} --description {{My snapshot description}}`

- 删除容器并移除所有相关资源：

`pct destroy {{100}} --purge`
