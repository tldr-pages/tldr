# taskkill

> 按进程id或进程名终止进程.

- 通过进程id终止进程:

`taskkill /pid {{进程id}}`

- 通过进程名终止进程:

`taskkill /im {{进程名}}`

- 强制终止一个指定的进程:

`taskkill /pid {{进程名}} /f`

- 终止一个进程及其子进程:

`taskkill /im {{进程名}} /t`

- 终止远程计算机上的进程:

`taskkill /pid {{进程id}} /s {{远程主机名}}`

- 显示命令的帮助信息:

`taskkill /?`
