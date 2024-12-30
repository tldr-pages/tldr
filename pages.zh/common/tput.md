# tput

> 查看和修改终端设置和功能。
> 更多信息：<https://manned.org/tput>。

- 将光标移动到屏幕位置：

`tput cup {{row}} {{column}}`

- 设置前景色 (af) 或背景色 (ab)：

`tput {{setaf|setab}} {{ansi_color_code}}`

- 显示列数、行数或颜色数：

`tput {{cols|lines|colors}}`

- 发出终端铃声：

`tput bel`

- 重置所有终端属性：

`tput sgr0`

- 启用或禁用换行：

`tput {{smam|rmam}}`