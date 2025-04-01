# grim

> 从 Wayland 合成器抓取图像（截图）。
> 更多信息：<https://sr.ht/~emersion/grim>.

- 截取所有输出的屏幕：

`grim`

- 截取特定输出的屏幕：

`grim -o {{path/to/output_file}}`

- 截取特定区域的屏幕：

`grim -g "{{x_position}},{{y_position}} {{width}}x{{height}}"`

- 选择特定区域并截取屏幕（使用 slurp）：

`grim -g "{{$(slurp)}}"`

- 使用自定义文件名：

`grim "{{path/to/file.png}}"`

- 截取屏幕并复制到剪贴板：

`grim - | {{clipboard_manager}}`