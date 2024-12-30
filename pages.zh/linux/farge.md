# farge

> 在屏幕上以十六进制或RGB格式显示特定像素的颜色。
> 更多信息：<https://github.com/sdushantha/farge>。

- 显示一个像素颜色的小预览窗口及其十六进制值，并将该值复制到剪贴板：

`farge`

- 在不显示预览窗口的情况下，将像素的十六进制值复制到剪贴板：

`farge --no-preview`

- 将像素的十六进制值输出到 `stdout`，并将该值复制到剪贴板：

`farge --stdout`

- 将像素的RGB值输出到 `stdout`，并将该值复制到剪贴板：

`farge --rgb --stdout`

- 将像素的十六进制值作为通知显示，通知在5000毫秒后过期，并将该值复制到剪贴板：

`farge --notify --expire-time 5000`