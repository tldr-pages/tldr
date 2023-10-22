# more

> 分页显示标准输入或文件的输出。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- 分页显示标准输入的输出：

`{{echo test}} | more`

- 分页显示一个或多个文件的内容：

`more {{文件的路径}}`

- 将制表符转换为指定的空格数：

`more {{文件的路径}} /t{{空格数}}`

- 显示内容前先清屏：

`more {{文件的路径}} /c`

- 从第 5 行开始显示输出：

`more {{文件的路径}} +{{5}}`

- 启用扩展交互模式（请参阅使用帮助）：

`more {{文件的路径}} /e`

- 显示全部帮助信息：

`more /?`
