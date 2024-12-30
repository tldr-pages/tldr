# st-util

> 运行 GDB（GNU 调试器）服务器以与 STM32 ARM Cortex 微控制器进行交互。
> 更多信息：<https://github.com/texane/stlink>。

- 在 4500 端口上运行 GDB 服务器：

`st-util -p {{4500}}`

- 连接到 GDB 服务器：

`(gdb) target extended-remote {{localhost}}:{{4500}}`

- 将固件写入设备：

`(gdb) load {{firmware.elf}}`