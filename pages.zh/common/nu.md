# nu

> Nushell（“一种新型的 Shell”）采用现代且结构化的方式处理命令行。
> 参见：`elvish`。
> 更多信息：<https://www.nushell.sh>。

- 启动交互式 Shell 会话：

`nu`

- 执行特定命令：

`nu --commands "{{echo 'nu is executed'}}"`

- 执行特定脚本：

`nu {{path/to/script.nu}}`

- 执行特定脚本并记录日志：

`nu --log-level {{error|warn|info|debug|trace}} {{path/to/script.nu}}`
