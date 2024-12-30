# neofetch

> 显示有关您的操作系统、软件和硬件的信息。
> 更多信息：<https://github.com/dylanaraps/neofetch>。

- 返回默认配置，如果这是程序第一次运行，则创建它：

`neofetch`

- 触发信息行在输出中出现，其中 'infoname' 是配置文件中的函数名称，例如内存：

`neofetch --{{enable|disable}} {{infoname}}`

- 隐藏/显示操作系统架构：

`neofetch --os_arch {{on|off}}`

- 启用/禁用输出中的 CPU 品牌：

`neofetch --cpu_brand {{on|off}}`