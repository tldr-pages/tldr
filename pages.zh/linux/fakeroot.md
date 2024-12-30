# fakeroot

> 在一个伪装为根权限的环境中运行命令以进行文件操作。
> 更多信息：<https://manned.org/fakeroot.1>。

- 以 fakeroot 启动默认 shell：

`fakeroot`

- 以 fakeroot 运行命令：

`fakeroot -- {{command}} {{command_arguments}}`

- 以 fakeroot 运行命令并在退出时将环境保存到文件：

`fakeroot -s {{path/to/file}} -- {{command}} {{command_arguments}}`

- 加载 fakeroot 环境并以 fakeroot 运行命令：

`fakeroot -i {{path/to/file}} -- {{command}} {{command_arguments}}`

- 运行命令时保持文件的真实所有权，而不是假装它们属于根用户：

`fakeroot --unknown-is-real -- {{command}} {{command_arguments}}`

- 显示帮助信息：

`fakeroot --help`