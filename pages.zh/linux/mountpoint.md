# mountpoint

> 检查目录是否为文件系统挂载点。
> 更多信息：<https://manned.org/mountpoint>.

- 检查目录是否为挂载点：

`mountpoint {{path/to/directory}}`

- 检查目录是否为挂载点而不显示任何输出：

`mountpoint {{[-q|--quiet]}} {{path/to/directory}}`

- 显示挂载点文件系统的主次设备号：

`mountpoint {{[-d|--fs-devno]}} {{path/to/directory}}`