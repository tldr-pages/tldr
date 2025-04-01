# tput

> 查看和修改终端设置和功能。
> 更多信息：<https://manned.org/tput>.

- 将光标移动到屏幕上的位置：

`tput cup {{row}} {{column}}`

- 设置前景色（af）或背景色（ab）：

`tput {{setaf|setab}} {{ansi_color_code}}`

- 反转文本和背景颜色：

`tput rev`

- 重置所有终端文本属性：

`tput sgr0`

- 显示列数、行数或颜色数：

`tput {{cols|lines|colors}}`

- 启用或禁用自动换行：

`tput {{smam|rmam}}`

- 隐藏或显示终端光标：

`tput {{civis|cnorm}}`

- 保存或恢复终端文本状态（smcup 还会捕获滚动轮事件）：

`tput {{smcup|rmcup}}`