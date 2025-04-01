# xdg-mime

> 根据 XDG 标准查询和管理 MIME 类型。
> 更多信息：<https://portland.freedesktop.org/doc/xdg-mime.html>。

- 显示文件的 MIME 类型：

`xdg-mime query filetype {{path/to/file}}`

- 显示用于打开 PNG 文件的默认应用程序：

`xdg-mime query default {{image/png}}`

- 显示用于打开特定文件的默认应用程序：

`xdg-mime query default $(xdg-mime query filetype {{path/to/file}})`

- 将 imv 设置为打开 PNG 和 JPEG 图像的默认应用程序：

`xdg-mime default {{imv.desktop}} {{image/png}} {{image/jpeg}}`
