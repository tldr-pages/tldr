# wodim

> 用于将数据录制到CD或DVD的命令（在某些系统上别名为`cdrecord`）。
> 一些wodim的调用可能会导致破坏性操作，例如擦除光盘上的所有数据。
> 更多信息：<https://manned.org/wodim>。

- 显示可用于`wodim`的光驱：

`wodim --devices`

- 录制（“烧录”）音频光盘：

`wodim dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- 将文件烧录到光盘，在完成后弹出光盘（某些录音机需要这样操作）：

`wodim -eject dev={{/dev/optical_drive}} -data {{file.iso}}`

- 将文件烧录到光驱中的光盘，可能连续写入多个光盘：

`wodim -tao dev={{/dev/optical_drive}} -data {{file.iso}}`