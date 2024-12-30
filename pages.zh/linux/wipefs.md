# wipefs

> 从设备中清除文件系统、RAID或分区表签名。
> 更多信息：<https://manned.org/wipefs>。

- 显示指定设备的签名：

`sudo wipefs {{/dev/sdX}}`

- 清除特定设备的所有可用签名类型，不递归到分区：

`sudo wipefs --all {{/dev/sdX}}`

- 使用通配符模式清除设备及其分区的所有可用签名类型：

`sudo wipefs --all {{/dev/sdX}}*`

- 进行干运行：

`sudo wipefs --all --no-act {{/dev/sdX}}`

- 强制清除，即使文件系统已挂载：

`sudo wipefs --all --force {{/dev/sdX}}`