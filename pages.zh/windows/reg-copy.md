# reg copy

> 复制注册表中的键及其值。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-copy>。

- 将注册表键复制到新的注册表位置：

`reg copy {{old_key_name}} {{new_key_name}}`

- 递归地复制注册表键（包括所有 [子]键）到新的注册表位置：

`reg copy {{old_key_name}} {{new_key_name}} /s`

- [强制]（无提示）复制注册表键：

`reg copy {{old_key_name}} {{new_key_name}} /f`