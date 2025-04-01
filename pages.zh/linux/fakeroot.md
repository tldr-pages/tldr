# fakeroot

> 在一个模拟根权限的环境中运行命令，用于文件操作。
> 更多信息：<https://manned.org/fakeroot.1>.

- 以 fakeroot 身份启动默认 shell：

`fakeroot`

- 以 fakeroot 身份运行命令：

`fakeroot -- {{command}} {{command_arguments}}`

- 以 fakeroot 身份运行命令，并在退出时将环境保存到文件中：

`fakeroot -s {{path/to/file}} -- {{command}} {{command_arguments}}`

- 加载 fakeroot 环境并以 fakeroot 身份运行命令：

`fakeroot -i {{path/to/file}} -- {{command}} {{command_arguments}}`

- 以保持文件的实际所有权而不是假装它们属于 root 的方式运行命令：

`fakeroot --unknown-is-real -- {{command}} {{command_arguments}}`

- 显示帮助信息：

`fakeroot --help`