# screenkey

> 一款用于显示按下键的屏幕录制工具。
> 更多信息：<https://www.thregr.org/~wavexx/software/screenkey/>.

- 在屏幕上显示当前按下的键：

`screenkey`

- 在屏幕上显示当前按下的键和鼠标按钮：

`screenkey --mouse`

- 启动screenkey的设置菜单：

`screenkey --show-settings`

- 在特定位置启动screenkey：

`screenkey --position {{top|center|bottom|fixed}}`

- 更改屏幕上显示的键修改器格式：

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- 更改screenkey的外观：

`screenkey --bg-color "{{#a1b2c3}}" --font {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- 在屏幕上拖动并选择一个窗口以显示screenkey：

`screenkey --position fixed --geometry {{$(slop -n -f '%g')}}`