# scd

> 专注于Shell集成的文件管理器。
> 更多信息：<https://github.com/cshuaimin/scd>。

- 第一次运行时递归索引路径：

`scd -ar {{path/to/directory}}`

- 切换到特定目录：

`scd {{path/to/directory}}`

- 切换到匹配特定模式的路径：

`scd "{{pattern1 pattern2 ...}}"`

- 显示选择菜单和20个最可能目录的排名：

`scd -v`

- 为当前目录添加特定别名：

`scd --alias={{word}}`

- 使用特定别名切换到目录：

`scd {{word}}`