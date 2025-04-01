# conky

> 轻量级的 X 系统监视器。
> 更多信息：<https://github.com/brndnmtthws/conky>.

- 使用默认的内置配置启动：

`conky`

- 创建一个新的默认配置文件：

`conky -C > ~/.conkyrc`

- 使用指定的配置文件启动 Conky：

`conky -c {{path/to/config}}`

- 以后台模式启动（守护进程）：

`conky -d`

- 在桌面上对齐 Conky：

`conky -a {{top|bottom|middle}}_{{left|right|middle}}`

- 启动时暂停 5 秒：

`conky -p {{5}}`