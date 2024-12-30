# stty

> 设置终端设备接口的选项。
> 更多信息：<https://www.gnu.org/software/coreutils/stty>。

- 显示当前终端的所有设置：

`stty --all`

- 设置行数或列数：

`stty {{rows|cols}} {{count}}`

- 获取设备的实际传输速度：

`stty --file {{path/to/device_file}} speed`

- 将所有模式重置为当前终端的合理值：

`stty sane`