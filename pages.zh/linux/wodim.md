# wodim

> 用于将数据刻录到 CD 或 DVD 的命令（在某些系统中别名为 `cdrecord`）。
> wodim 的某些用法可能导致破坏性操作，例如擦除光盘上的所有数据。
> 更多信息：<https://manned.org/wodim>.

- 显示 wodim 可用的光驱：

`wodim --devices`

- 刻录音频光盘：

`wodim dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- 将文件刻录到光盘，并在完成后弹出光盘（某些刻录机需要此操作）：

`wodim -eject dev={{/dev/optical_drive}} -data {{file.iso}}`

- 将文件刻录到光驱中的光盘，可以连续刻录多张光盘：

`wodim -tao dev={{/dev/optical_drive}} -data {{file.iso}}`