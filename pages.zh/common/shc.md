# shc

> 通用的 Shell 脚本编译器。
> 更多信息：<https://manned.org/shc>.

- 编译一个 Shell 脚本：

`shc -f {{script}}`

- 编译一个 Shell 脚本并指定输出的二进制文件：

`shc -f {{script}} -o {{binary}}`

- 编译一个 Shell 脚本并为可执行文件设置过期日期：

`shc -f {{script}} -e {{dd/mm/yyyy}}`

- 编译一个 Shell 脚本并设置过期时显示的消息：

`shc -f {{script}} -e {{dd/mm/yyyy}} -m "{{请联系您的提供商}}"`
