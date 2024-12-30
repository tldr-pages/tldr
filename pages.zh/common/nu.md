# nu

> Nushell（“一种新型的命令行外壳”）采用现代化、结构化的方法来处理你的命令行。
> 另请参见：`elvish`。
> 更多信息：<https://www.nushell.sh>。

- 开始一个交互式的 shell 会话：

`nu`

- 执行特定命令：

`nu --commands "{{echo 'nu 被执行'}}"`

- 执行特定脚本：

`nu {{path/to/script.nu}}`

- 执行特定脚本并记录日志：

`nu --log-level {{error|warn|info|debug|trace}} {{path/to/script.nu}}`