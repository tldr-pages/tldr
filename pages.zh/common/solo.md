# solo

> 与 Solo 硬件安全密钥交互。
> 更多信息：<https://github.com/solokeys/solo-python>.

- 列出已连接的 Solos:

`solo ls`

- 将当前连接的 Solo 的固件更新到最新版本:

`solo key update`

- 使特定 Solo 的 LED 闪烁:

`solo key wink --serial {{serial_number}}`

- 使用当前连接的 Solo 的安全随机数生成器生成随机字节:

`solo key rng raw`

- 监控 Solo 的串行输出:

`solo monitor {{path/to/serial_port}}`