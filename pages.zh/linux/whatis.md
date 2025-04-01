# whatis

> 显示来自手册页的一行描述。
> 更多信息：<https://manned.org/whatis>.

- 显示来自手册页的描述：

`whatis {{command}}`

- 不在行尾截断描述：

`whatis --long {{command}}`

- 显示与通配符匹配的所有命令的描述：

`whatis --wildcard {{net*}}`

- 使用正则表达式搜索手册页描述：

`whatis --regex '{{wish[0-9]\.[0-9]}}'`

- 以特定语言显示描述：

`whatis --locale={{en}} {{command}}`
