# qm disk import

> 将磁盘映像作为未使用的磁盘导入到虚拟机中。
> 支持 `qemu-img` 的图像格式，如 raw、qcow2、qed、vdi、vmdk 和 vhd。
> 更多信息：<https://pve.proxmox.com/pve-docs/qm.1.html>。

- 使用特定的存储名称导入 VMDK/qcow2/raw 磁盘映像：

`qm importdisk {{vm_id}} {{path/to/disk}} {{storage_name}} --format {{qcow2|raw|vmdk}}`
