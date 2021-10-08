# reg save

> 将注册表键、子键的所有值保存到一个文件中。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- 将注册表键、子键的所有值保存到一个文件中：

`reg save {{键名}} {{文件的路径}}`

- 在没有提示的情况下强制覆盖现有文件：

`reg save {{键名}} {{文件的路径}} /y`
