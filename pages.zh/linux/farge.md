# farge

> 显示屏幕上特定像素的颜色，颜色格式可以是十六进制或RGB。
> 更多信息：<https://github.com/sdushantha/farge>。

- 显示一个带有像素颜色十六进制值的小预览窗口，并将此值复制到剪贴板：

`farge`

- 不显示预览窗口，将像素的十六进制值复制到剪贴板：

`farge --no-preview`

- 将像素的十六进制值输出到 `stdout`，并将此值复制到剪贴板：

`farge --stdout`

- 将像素的RGB值输出到 `stdout`，并将此值复制到剪贴板：

`farge --rgb --stdout`

- 以通知的形式显示像素的十六进制值，通知在5000毫秒后过期，并将此值复制到剪贴板：

`farge --notify --expire-time 5000`
