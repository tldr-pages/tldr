# slop

> 获取屏幕的选择区域。
> 更多信息：<https://github.com/naelstrof/slop>。

- 等待用户进行选择，并将其几何信息输出到 `stdout`：

`slop`

- 双击而不是点击并拖动来绘制选择区域：

`slop -D`

- 高亮选择区域而不是勾勒其轮廓：

`slop -l`

- 指定输出格式：

`slop -f {{format_string}}`

- 指定选择矩形的颜色：

`slop -c {{red}},{{green}},{{blue}},{{alpha}}`