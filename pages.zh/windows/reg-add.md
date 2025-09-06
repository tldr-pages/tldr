# reg add

> 将新的键值添加到注册表中。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- 添加一个新的注册表键：

`reg add {{键名}}`

- 在指定的键下添加新值：

`reg add {{键名}} /v {{值}}`

- Add a new value with specific data：

`reg add {{键名}} /d {{数据}}`

- 向具有特定数据类型的键添加新值：

`reg add {{键名}} /t {{类型}}`

- 在没有提示的情况下强制覆盖现有的注册表值：

`reg add {{键名}} /f`
