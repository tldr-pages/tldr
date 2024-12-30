# bcachefs 设备

> 管理正在运行的 `bcachefs` 文件系统中的设备。
> 更多信息：<https://bcachefs-docs.readthedocs.io/en/latest/mgmt-devicemanagement.html>。

- 格式化并将新设备添加到现有文件系统中：

`sudo bcachefs device add --label={{group}}.{{name}} {{path/to/mountpoint}} {{path/to/device}}`

- 将数据迁移出设备以准备移除：

`bcachefs device evacuate {{path/to/device}}`

- 永久性地从文件系统中移除设备：

`bcachefs device remove {{path/to/device}}`