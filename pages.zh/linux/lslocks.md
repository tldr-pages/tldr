# lslocks

> 列出本地系统锁。
> 更多信息: <https://manned.org/lslocks>.

- 列出所有本地系统锁：

`lslocks`

- 列出带有定义的列标题的锁：

`lslocks {{[-o|--output]}} {{PID}},{{COMMAND}},{{PATH}}`

- 列出锁，输出原始数据（无列），且不包含列标题：

`lslocks {{[-r|--raw]}} {{[-n|--noheadings]}}`

- 按 PID 输入列出锁：

`lslocks {{[-p|--pid]}} {{PID}}`

- 列出锁，并以 JSON 格式输出到 `stdout`：

`lslocks {{[-J|--json]}}`