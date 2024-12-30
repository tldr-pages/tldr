# conky

> 轻量级系统监视器，适用于 X。
> 更多信息：<https://github.com/brndnmtthws/conky>。

- 使用默认的内置配置启动：

`conky`

- 创建一个新的默认配置：

`conky -C > ~/.conkyrc`

- 使用指定的配置文件启动 Conky：

`conky -c {{path/to/config}}`

- 在后台启动 (守护进程化)：

`conky -d`

- 在桌面上对齐 Conky：

`conky -a {{top|bottom|middle}}_{{left|right|middle}}`

- 启动时暂停 5 秒后再启动：

`conky -p {{5}}`