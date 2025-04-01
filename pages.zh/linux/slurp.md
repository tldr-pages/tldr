# slurp

> 在 Wayland 合成器中选择一个区域。
> 更多信息：<https://github.com/emersion/slurp>.

- 选择一个区域并将其输出到 `stdout`：

`slurp`

- 选择一个区域并将其输出到 `stdout`，同时显示选择区域的尺寸：

`slurp -d`

- 选择一个点而不是区域：

`slurp -p`

- 选择一个输出并输出其名称：

`slurp -o -f '%o'`

- 选择一个特定区域并使用 `grim` 截取无边框的屏幕截图：

`grim -g "$(slurp -w 0)"`

- 选择一个特定区域并使用 `wf-recorder` 录制无边框的视频：

`wf-recorder --geometry "$(slurp -w 0)"`