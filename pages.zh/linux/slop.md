# slop

> 获取屏幕选择区域。
> 更多信息：<https://github.com/naelstrof/slop>。

- 等待用户选择区域，并将其几何信息输出到 `stdout`：

`slop`

- 双击而非点击并拖动来绘制选择区域：

`slop -D`

- 突出显示选择区域而不是只绘制边框：

`slop -l`

- 指定输出格式：

`slop -f {{format_string}}`

- 指定选择矩形的颜色：

`slop -c {{red}},{{green}},{{blue}},{{alpha}}`
