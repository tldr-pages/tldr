# mt

> 控制磁带驱动器操作（通常是LTO磁带）。
> 更多信息请访问: <https://manned.org/mt>。

- 检查磁带驱动器的状态：

`mt -f {{/dev/nstX}} status`

- 将磁带倒带到开头：

`mt -f {{/dev/nstX}} rewind`

- 向前移动指定的文件，然后将磁带定位到下一个文件的第一个块：

`mt -f {{/dev/nstX}} fsf {{count}}`

- 倒带磁带，然后将磁带定位到指定文件的开头：

`mt -f {{/dev/nstX}} asf {{count}}`

- 将磁带定位到有效数据的末尾：

`mt -f {{/dev/nstX}} eod`

- 倒带磁带并卸载/弹出它：

`mt -f {{/dev/nstX}} eject`

- 在当前位置写入EOF（文件结束）标记：

`mt -f {{/dev/nstX}} eof`