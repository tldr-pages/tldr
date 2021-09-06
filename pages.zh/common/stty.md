# stty

> 设置终端设备接口的选项。
> 更多信息：<https://www.gnu.org/software/coreutils/stty>.

- 显示当前终端的所有设置：

`stty -a`

- 设置行数：

`stty rows {{行数}}`

- 设置列数：

`stty cols {{列数}}`

- 获取设备的实际传输速度：

`stty -F {{目标 / 文件夹 / 驱动设备文件}} speed`

- 将当前终端的所有模式重置为合理值：

`stty sane`
