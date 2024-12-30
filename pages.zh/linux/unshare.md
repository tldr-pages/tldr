# unshare

> 在新的用户定义命名空间中执行命令。
> 更多信息请访问: <https://www.kernel.org/doc/html/latest/userspace-api/unshare.html>。

- 执行命令时不共享连接网络的访问权限：

`unshare --net {{command}} {{command_arguments}}`

- 作为子进程执行命令，不共享挂载、进程或网络：

`unshare --mount --pid --net --fork {{command}} {{command_arguments}}`