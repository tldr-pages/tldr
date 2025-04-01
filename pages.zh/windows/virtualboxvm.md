# virtualboxvm

> 管理 VirtualBox 虚拟机。
> 更多信息：<https://www.virtualbox.org>.

- 启动虚拟机：

`virtualboxvm --startvm {{name|uuid}}`

- 以全屏模式启动虚拟机：

`virtualboxvm --startvm {{name|uuid}} --fullscreen`

- 挂载指定的 DVD 镜像文件：

`virtualboxvm --startvm {{name|uuid}} --dvd {{path\to\image_file}}`

- 显示带有调试信息的命令行窗口：

`virtualboxvm --startvm {{name|uuid}} --debug-command-line`

- 以暂停状态启动虚拟机：

`virtualboxvm --startvm {{name|uuid}} --start-paused`