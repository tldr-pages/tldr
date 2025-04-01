# st-flash

> 将二进制文件烧录到 STM32 ARM Cortex 微控制器中。
> 更多信息：<https://github.com/texane/stlink>。

- 从 0x8000000 地址开始读取 4096 字节的数据到文件：

`st-flash read {{firmware}}.bin {{0x8000000}} {{4096}}`

- 从 0x8000000 地址开始将固件写入设备：

`st-flash write {{firmware}}.bin {{0x8000000}}`

- 从设备中擦除固件：

`st-flash erase`
