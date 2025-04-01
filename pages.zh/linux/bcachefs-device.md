# bcachefs device

> 管理正在运行的 `bcachefs` 文件系统中的设备。
> 更多信息：<https://bcachefs-docs.readthedocs.io/en/latest/mgmt-devicemanagement.html>.

- 格式化并添加新设备到现有文件系统：

`sudo bcachefs device add --label={{group}}.{{name}} {{/路径/到/挂载点}} {{/路径/到/设备}}`

- 将数据从设备迁移出去，为移除设备做准备：

`bcachefs device evacuate {{/路径/到/设备}}`

- 从文件系统中永久移除设备：

`bcachefs device remove {{/路径/到/设备}}`