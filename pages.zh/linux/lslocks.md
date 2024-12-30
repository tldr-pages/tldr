# lslocks

> 列出本地系统锁。
> 更多信息：<https://manned.org/lslocks>。

- 列出所有本地系统锁：

`lslocks`

- 列出带有定义列标题的锁：

`lslocks --output {{PID}},{{COMMAND}},{{PATH}}`

- 列出产生原始输出（没有列），且没有列标题的锁：

`lslocks --raw --noheadings`

- 根据PID输入列出锁：

`lslocks --pid {{PID}}`

- 将锁以JSON格式输出到`stdout`：

`lslocks --json`