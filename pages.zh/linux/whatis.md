# whatis

> 从手册页显示一行描述。
> 更多信息：<https://manned.org/whatis>。

- 从手册页显示描述：

`whatis {{command}}`

- 不要在行末截断描述：

`whatis --long {{command}}`

- 显示所有匹配通配符的命令描述：

`whatis --wildcard {{net*}}`

- 使用正则表达式搜索手册页描述：

`whatis --regex '{{wish[0-9]\.[0-9]}}'`

- 以特定语言显示描述：

`whatis --locale={{en}} {{command}}`