# flips

> 创建并应用IPS和BPS文件的补丁。
> 更多信息：<https://github.com/Alcaro/Flips>。

- 启动Flips以交互方式创建和应用补丁：

`flips`

- 应用补丁并创建新的ROM文件：

`flips --apply {{patch.bps}} {{rom.smc}} {{hack.smc}}`

- 从两个ROM创建补丁：

`flips --create {{rom.smc}} {{hack.smc}} {{patch.bps}}`