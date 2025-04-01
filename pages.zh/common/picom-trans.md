# picom-trans

> 为 `picom` 窗口合成器设置窗口不透明度。
> 更多信息：<https://github.com/yshui/picom>。

- 设置当前焦点窗口的不透明度为特定百分比：

`picom-trans --current --opacity {{90}}`

- 设置特定名称窗口的不透明度：

`picom-trans --name {{Firefox}} --opacity {{90}}`

- 通过鼠标选择特定窗口并设置其不透明度：

`picom-trans --select --opacity {{90}}`

- 切换特定窗口的不透明度：

`picom-trans --name {{Firefox}} --toggle`