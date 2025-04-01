# scd

> 专注于 Shell 集成的文件管理器。
> 更多信息：<https://github.com/cshuaimin/scd>。

- 首次运行时递归索引路径：

`scd -ar {{path/to/directory}}`

- 切换到特定目录：

`scd {{path/to/directory}}`

- 切换到与特定模式匹配的路径：

`scd "{{pattern1 pattern2 ...}}"`

- 显示选择菜单和排名前 20 的目录：

`scd -v`

- 为当前目录添加特定的别名：

`scd --alias={{word}}`

- 使用特定别名切换到目录：

`scd {{word}}`
