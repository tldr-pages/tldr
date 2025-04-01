# wipefs

> 从设备中擦除文件系统、RAID 或分区表签名。
> 更多信息：<https://manned.org/wipefs>.

- 显示指定设备的签名：

`sudo wipefs {{/dev/sdX}}`

- 擦除特定设备的所有可用签名类型，不递归到分区中：

`sudo wipefs {{[-a|--all]}} {{/dev/sdX}}`

- 使用通配符模式擦除设备及其分区的所有可用签名类型：

`sudo wipefs {{[-a|--all]}} {{/dev/sdX}}*`

- 执行干运行（不实际执行擦除操作）：

`sudo wipefs {{[-a|--all]}} {{[-n|--no-act]}} {{/dev/sdX}}`

- 强制擦除，即使文件系统已挂载：

`sudo wipefs {{[-a|--all]}} {{[-f|--force]}} {{/dev/sdX}}`
