# xset

> X 的用户偏好设置工具。
> 更多信息：<https://manned.org/xset>.

- 禁用屏幕保护程序：

`xset s off`

- 禁用铃声：

`xset b off`

- 设置屏幕保护程序在 60 分钟无活动后启动：

`xset s 3600 3600`

- 禁用 DPMS（能源之星）功能：

`xset -dpms`

- 启用 DPMS（能源之星）功能：

`xset +dpms`

- 查询任何 X 服务器的信息：

`xset -display :{{0}} q`
