# slurp

> 在 Wayland 合成器中选择一个区域。
> 更多信息：<https://github.com/emersion/slurp>。

- 选择一个区域并将其打印到 `stdout`：

`slurp`

- 选择一个区域并将其打印到 `stdout`，同时显示选择的尺寸：

`slurp -d`

- 选择一个点而不是一个区域：

`slurp -p`

- 选择一个输出并打印其名称：

`slurp -o -f '%o'`

- 选择一个特定区域并使用 `grim` 进行无边框截图：

`grim -g "$(slurp -w 0)"`

- 选择一个特定区域并使用 `wf-recorder` 进行无边框视频录制：

`wf-recorder --geometry "$(slurp -w 0)"`