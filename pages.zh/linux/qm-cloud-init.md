# qm cloud init

> 为 Proxmox Virtual Environment (PVE) 管理的虚拟机配置 cloudinit 设置。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>.

- 为特定用户配置 cloudinit 设置并设置该用户的密码：

`qm cloud-init {{vm_id}} -user={{user}} -password={{password}}`

- 为特定用户配置 cloudinit 设置并使用特定的 SSH 密钥设置该用户的密码：

`qm cloud-init {{vm_id}} -user={{user}} -password={{password}} -sshkey={{ssh_key}}`

- 为特定虚拟机设置主机名：

`qm cloud-init {{vm_id}} -hostname={{hostname}}`

- 为特定虚拟机配置网络接口设置：

`qm cloud-init {{vm_id}} -ipconfig {{ipconfig}}`

- 配置一个脚本，在虚拟机上运行 `cloud-ini` 之前执行：

`qm cloud-init {{vm_id}} -pre {{script}}`
