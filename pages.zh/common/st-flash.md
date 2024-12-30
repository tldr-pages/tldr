# st-flash

> 将二进制文件闪存到STM32 ARM Cortex微控制器。
> 更多信息：<https://github.com/texane/stlink>。

- 从设备的0x8000000地址开始读取4096字节：

`st-flash read {{firmware}}.bin {{0x8000000}} {{4096}}`

- 从0x8000000地址开始将固件写入设备：

`st-flash write {{firmware}}.bin {{0x8000000}}`

- 从设备中擦除固件：

`st-flash erase`