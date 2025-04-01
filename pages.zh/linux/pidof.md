# pidof

> 通过进程名称获取进程ID。
> 更多信息：<https://manned.org/pidof>.

- 列出给定名称的所有进程ID：

`pidof {{bash}}`

- 列出给定名称的单个进程ID：

`pidof -s {{bash}}`

- 列出给定名称的进程ID，包括脚本：

`pidof -x {{script.py}}`

- 杀死所有给定名称的进程：

`kill $(pidof {{name}})`
