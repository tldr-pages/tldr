# pidof

> 使用进程名获取进程ID。
> 更多信息：<https://manned.org/pidof>。

- 列出所有具有给定名称的进程ID：

`pidof {{bash}}`

- 列出具有给定名称的单个进程ID：

`pidof -s {{bash}}`

- 列出包括脚本在内的具有给定名称的进程ID：

`pidof -x {{script.py}}`

- 杀死所有具有给定名称的进程：

`kill $(pidof {{name}})`