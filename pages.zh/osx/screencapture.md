# screencapture

> 用于截取屏幕截图和屏幕录制。
> 更多信息：<https://keith.github.io/xcode-man-pages/screencapture.1.html>。

- 截取屏幕截图并保存到文件：

`screencapture {{path/to/file.png}}`

- 截取包含鼠标指针的屏幕截图：

`screencapture -C {{path/to/file.png}}`

- 截取屏幕截图并在预览中打开，而不是保存：

`screencapture -P`

- 截取选定矩形区域的屏幕截图：

`screencapture -i {{path/to/file.png}}`

- 延迟若干秒后截取屏幕截图：

`screencapture -T {{seconds}} {{path/to/file.png}}`

- 录制屏幕并保存到文件：

`screencapture -v {{path/to/file.mp4}}`
