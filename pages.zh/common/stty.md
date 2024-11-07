# stty

> 设置终端设备接口的选项。
> 更多信息：<https://www.gnu.org/software/coreutils/stty>.

- 显示当前终端的所有设置：

`stty --all`

- 设置行数或列数：

`stty {{行数|列数}} {{数量}}`

- 获取设备的实际传输速度：

`stty --file {{路径/到/驱动设备文件}} speed`

- 重置所有模式为当前终端的合理默认值：

`stty sane`
