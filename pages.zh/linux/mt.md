# mt

> 控制磁带驱动器的运行（通常是 LTO 磁带）。
> 更多信息：<https://manned.org/mt>。

- 检查磁带驱动器的状态：

`mt -f {{/dev/nstX}} status`

- 将磁带倒回开头：

`mt -f {{/dev/nstX}} rewind`

- 向前移动指定的文件数，然后将磁带定位到下一个文件的第一个块：

`mt -f {{/dev/nstX}} fsf {{count}}`

- 将磁带倒回，然后将磁带定位到指定文件的开头：

`mt -f {{/dev/nstX}} asf {{count}}`

- 将磁带定位到有效数据的末尾：

`mt -f {{/dev/nstX}} eod`

- 倒回磁带并卸载/弹出磁带：

`mt -f {{/dev/nstX}} eject`

- 在当前位置写入 EOF（文件结束）标记：

`mt -f {{/dev/nstX}} eof`