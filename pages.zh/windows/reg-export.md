# reg export

> 将指定的子键和值导出到文件中。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- 导出指定键下所有的子键和值：

`reg export {{键名}} {{导出文件的路径.reg}}`

- 在没有提示的情况下强制覆盖现有文件：

`reg export {{键名}} {{导出文件的路径.reg}} /y`
