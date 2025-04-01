# hwinfo

> 检测系统中存在硬件的信息。
> 更多信息：<https://manpages.opensuse.org/hwinfo/hwinfo.8.en.html>。

- 获取显卡信息：

`hwinfo --gfxcard`

- 获取网络设备信息：

`hwinfo --network`

- 列出硬盘和光驱，简化输出：

`hwinfo --short --disk --cdrom`

- 将所有硬件信息写入文件：

`hwinfo --all --log {{path/to/file}}`

- 显示帮助：

`hwinfo --help`