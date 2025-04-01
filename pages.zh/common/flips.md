# flips

> 创建和应用 IPS 和 BPS 文件的补丁。
> 更多信息：<https://github.com/Alcaro/Flips>.

- 启动 Flips 以交互方式创建和应用补丁：

`flips`

- 应用补丁并创建新的 ROM 文件：

`flips --apply {{patch.bps}} {{rom.smc}} {{hack.smc}}`

- 从两个 ROM 文件创建补丁：

`flips --create {{rom.smc}} {{hack.smc}} {{patch.bps}}`
