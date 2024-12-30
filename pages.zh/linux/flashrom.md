# flashrom

> 读取、写入、验证和擦除闪存芯片。
> 更多信息：<https://manned.org/flashrom>。

- 探测芯片，确保接线正确：

`flashrom --programmer {{programmer}}`

- 读取闪存并保存到文件：

`flashrom -p {{programmer}} --read {{path/to/file}}`

- 将文件写入闪存：

`flashrom -p {{programmer}} --write {{path/to/file}}`

- 将闪存与文件进行验证：

`flashrom -p {{programmer}} --verify {{path/to/file}}`

- 使用树莓派探测芯片：

`flashrom -p {{linux_spi:dev=/dev/spidev0.0}}`