# btm

> `top` 的替代品。
> 旨在轻量级、跨平台，并且比 `top` 更具图形化。
> 更多信息：<https://github.com/ClementTsang/bottom>。

- 显示默认布局（CPU、内存、温度、磁盘、网络和进程）：

`btm`

- 启用基本模式，移除图表并压缩数据（类似于 `top`）：

`btm --basic`

- 在图表中使用大点而不是小点：

`btm --dot_marker`

- 还显示电池充电和健康状态：

`btm --battery`

- 每250毫秒刷新一次，并在图表中显示最近30秒的数据：

`btm --rate 250 --default_time_value 30000`