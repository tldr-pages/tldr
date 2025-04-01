# cam

> `libcamera` 的前端工具。
> 更多信息：<https://libcamera.org/docs.html>.

- 列出可用的摄像头：

`cam {{[-l|--list]}}`

- 列出摄像头的控制选项：

`cam {{[-c|--camera]}} {{camera_index}} --list-controls`

- 将帧写入文件夹：

`cam {{[-c|--camera]}} {{camera_index}} {{[-C|--capture=]}}{{frames_to_capture}} {{[-F|--file]}}`

- 在窗口中显示摄像头画面：

`cam {{[-c|--camera]}} {{camera_index}} {{[-C|--capture]}} {{[-S|--sdl]}}`
