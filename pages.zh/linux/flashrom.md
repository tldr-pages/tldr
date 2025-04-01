# flashrom

> 读取、写入、验证和擦除闪存芯片。
> 更多信息：<https://manned.org/flashrom>。

- 检测芯片，确保线路正确：

`flashrom --programmer {{programmer}}`

- 读取闪存并将内容保存到文件：

`flashrom -p {{programmer}} --read {{path/to/file}}`

- 将文件写入闪存：

`flashrom -p {{programmer}} --write {{path/to/file}}`

- 验证闪存内容是否与文件一致：

`flashrom -p {{programmer}} --verify {{path/to/file}}`

- 使用 Raspberry Pi 检测芯片：

`flashrom -p {{linux_spi:dev=/dev/spidev0.0}}`
