# cam

> `libcamera` 的前端工具。
> 更多信息请访问：<https://libcamera.org/docs.html>。

- 列出可用的相机：

`cam --list`

- 列出相机的控制选项：

`cam --camera {{camera_index}} --list-controls`

- 将帧写入文件夹：

`cam --camera {{camera_index}} --capture={{frames_to_capture}} --file`

- 在窗口中显示相机画面：

`cam --camera {{camera_index}} --capture --sdl`