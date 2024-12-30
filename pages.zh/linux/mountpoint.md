# 挂载点

> 测试一个目录是否为文件系统挂载点。
> 更多信息：<https://manned.org/mountpoint>。

- 检查一个目录是否为挂载点：

`mountpoint {{path/to/directory}}`

- 检查一个目录是否为挂载点而不显示任何输出：

`mountpoint -q {{path/to/directory}}`

- 显示挂载点文件系统的主/次设备号：

`mountpoint --fs-devno {{path/to/directory}}`