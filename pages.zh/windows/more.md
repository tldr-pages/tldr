# more

> 从 `stdin` 或文件中显示分页输出。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/more>。

- 从 `stdin` 显示分页输出：

`{{echo test}} | more`

- 从一个或多个文件中显示分页输出：

`more {{path\to\file}}`

- 将制表符转换为指定数量的空格：

`more {{path\to\file}} /t{{spaces}}`

- 在显示页面之前清除屏幕：

`more {{path\to\file}} /c`

- 从第5行开始显示输出：

`more {{path\to\file}} +{{5}}`

- 启用扩展交互模式（有关用法，请参见帮助）：

`more {{path\to\file}} /e`

- 显示帮助：

`more /?`