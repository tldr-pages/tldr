# picom-trans

> 设置 `picom` 窗口合成器的窗口透明度。
> 更多信息：<https://github.com/yshui/picom>。

- 将当前聚焦窗口的透明度设置为特定百分比：

`picom-trans --current --opacity {{90}}`

- 将特定名称窗口的透明度设置为：

`picom-trans --name {{Firefox}} --opacity {{90}}`

- 将通过鼠标光标选择的特定窗口的透明度设置为：

`picom-trans --select --opacity {{90}}`

- 切换特定窗口的透明度：

`picom-trans --name {{Firefox}} --toggle`