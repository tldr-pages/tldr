# losetup

> 设置和控制循环设备。
> 更多信息：<https://manned.org/losetup>.

- 列出带有详细信息的循环设备：

`losetup {{[-a|--all]}}`

- 将文件挂载到指定的循环设备：

`sudo losetup {{/dev/loop}} /{{path/to/file}}`

- 将文件挂载到新的空闲循环设备，并扫描设备上的分区：

`sudo losetup --show {{[-P|--partscan]}} {{[-f|--find]}} /{{path/to/file}}`

- 将文件挂载到只读循环设备：

`sudo losetup {{[-r|--read-only]}} {{/dev/loop}} /{{path/to/file}}`

- 卸载所有循环设备：

`sudo losetup {{[-D|--detach-all]}}`

- 卸载指定的循环设备：

`sudo losetup {{[-d|--detach]}} {{/dev/loop}}`