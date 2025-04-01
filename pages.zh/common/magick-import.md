# magick import

> 捕获 X 服务器屏幕的一部分或全部，并将图像保存到文件中。
> 参见：`magick`。
> 更多信息：<https://imagemagick.org/script/import.php>。

- 捕获整个 X 服务器屏幕到 PostScript 文件中：

`magick import -window root {{path/to/output.ps}}`

- 捕获远程 X 服务器屏幕内容为 PNG 图像：

`magick import -window root -display {{remote_host}}:{{screen}}.{{display}} {{path/to/output.png}}`

- 根据 `xwininfo` 显示的窗口 ID 捕获特定窗口到 JPEG 图像：

`magick import -window {{window_id}} {{path/to/output.jpg}}`