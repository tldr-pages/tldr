# flameshot

> 带有图形用户界面的截图工具。
> 支持基本的图像编辑，如文本、形状、颜色和 imgur。
> 更多信息：<https://flameshot.org>。

- 创建全屏截图：

`flameshot full`

- 交互式创建截图：

`flameshot gui`

- 创建截图并保存到特定路径：

`flameshot gui --path {{path/to/directory}}`

- 以简化模式交互式创建截图：

`flameshot launcher`

- 从特定显示器创建截图：

`flameshot screen --number {{2}}`

- 创建截图并打印到 `stdout`：

`flameshot gui --raw`

- 创建截图并复制到剪贴板：

`flameshot gui --clipboard`

- 创建带有特定延迟（以毫秒为单位）的截图：

`flameshot full --delay {{5000}}`