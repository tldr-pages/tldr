# shc

> 通用的 shell 脚本编译器。
> 更多信息：<https://manned.org/shc>。

- 编译一个 shell 脚本：

`shc -f {{script}}`

- 编译一个 shell 脚本并指定输出的二进制文件：

`shc -f {{script}} -o {{binary}}`

- 编译一个 shell 脚本并设置可执行文件的到期日期：

`shc -f {{script}} -e {{dd/mm/yyyy}}`

- 编译一个 shell 脚本并设置到期时显示的消息：

`shc -f {{script}} -e {{dd/mm/yyyy}} -m "{{请联系您的服务提供商}}"`