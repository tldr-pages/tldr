# xprop

> 在 X 服务器中显示窗口和字体属性。
> 更多信息：<https://manned.org/xprop>.

- 显示根窗口的名称：

`xprop -root WM_NAME`

- 显示窗口的窗口管理器提示信息：

`xprop -name "{{window_name}}" WM_HINTS`

- 显示字体的点大小：

`xprop -font "{{font_name}}" POINT_SIZE`

- 显示 ID 为 0x200007 的窗口的所有属性：

`xprop -id {{0x200007}}`
