# losetup

> 设置和控制循环设备。
> 更多信息：<https://manned.org/losetup>。

- 列出循环设备及详细信息：

`losetup -a`

- 将文件附加到指定的循环设备：

`sudo losetup {{/dev/loop}} /{{path/to/file}}`

- 将文件附加到一个新的空闲循环设备并扫描设备的分区：

`sudo losetup --show --partscan -f /{{path/to/file}}`

- 将文件附加到只读循环设备：

`sudo losetup --read-only {{/dev/loop}} /{{path/to/file}}`

- 脱离所有循环设备：

`sudo losetup -D`

- 脱离指定的循环设备：

`sudo losetup -d {{/dev/loop}}`