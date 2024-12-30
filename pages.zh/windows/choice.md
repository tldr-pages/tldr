# 选择

> 提示用户选择一个选项并返回所选选项的索引。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/choice>。

- 提示当前用户选择 `Y` 或 `N` 选项：

`choice`

- 提示当前用户从特定集合中选择一个 [c]hoice：

`choice /c {{AB}}`

- 提示当前用户选择一个带有特定 [m]essage 的选项：

`choice /m "{{message}}"`

- 提示当前用户从特定集合中选择一个 [c]ase-[s]ensitive [c]hoice：

`choice /cs /c {{Ab}}`

- 提示当前用户选择一个选项，并在特定 [t]ime 内优先选择 [d]efault 选项：

`choice /t {{5}} /d {{N}}`

- 显示帮助：

`choice /?`