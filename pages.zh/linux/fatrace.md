# fatrace

> 报告文件访问事件。
> 更多信息： <https://manned.org/fatrace>.

- 在所有已挂载的文件系统中打印文件访问事件到 `stdout`：

`sudo fatrace`

- 在当前目录的挂载点打印带有时间戳的文件访问事件到 `stdout`：

`sudo fatrace {{[-c|--current-mount]}} {{[-t|--timestamp]}}`
