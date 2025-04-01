# screenkey

> 一个屏幕录制工具，用于显示按下的键。
> 更多信息：<https://www.thregr.org/~wavexx/software/screenkey/>。

- 显示屏幕上当前被按下的键：

`screenkey`

- 显示屏幕上当前被按下的键和鼠标按钮：

`screenkey --mouse`

- 启动 screenkey 的设置菜单：

`screenkey --show-settings`

- 在特定位置启动 screenkey：

`screenkey --position {{top|center|bottom|fixed}}`

- 更改屏幕上显示的键修饰符的格式：

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- 更改 screenkey 的外观：

`screenkey --bg-color "{{#a1b2c3}}" --font {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- 拖动并选择屏幕上的一个窗口来显示 screenkey：

`screenkey --position fixed --geometry {{$(slop -n -f '%g')}}`