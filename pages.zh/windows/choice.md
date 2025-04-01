# choice

> 提示用户选择一个选项，并返回所选选项的索引。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/choice>.

- 提示当前用户选择 `Y` 或 `N` 选项：

`choice`

- 提示当前用户从特定的集合中选择一个选项：

`choice /c {{AB}}`

- 提示当前用户带有特定消息的选择一个选项：

`choice /m "{{message}}"`

- 提示当前用户从特定集合中选择一个大小写敏感的选项：

`choice /cs /c {{Ab}}`

- 提示当前用户选择一个选项，并在特定时间内偏好某个默认选项：

`choice /t {{5}} /d {{default_choice}}`

- 显示帮助信息：

`choice /?`
