# btm

> 命令行`top`的替代品。
> 比 `top` 更轻便，支持跨平台、图表更丰富。
> 另请参阅：`btop`, `glances`, `atop`, `htop`, `top`, `sensors`。
> 更多信息：<https://clementtsang.github.io/bottom/nightly/#usage-and-configuration>。

- 展示默认布局（cpu, 内存，温度，磁盘，网络和 进程）：

`btm`

- 开启基础模式，关闭图表和高亮（接近于 `top`）：

`btm {{[-b|--basic]}}`

- 将图表中的小点换成大点：

`btm {{[-m|--dot_marker]}}`

- 展示电池充电和健康状态：

`btm --battery`

- 设置图表刷新间隔和留存数据的时长：

`btm {{[-r|--rate]}} 250 {{[-t|--default_time_value]}} 30000`
