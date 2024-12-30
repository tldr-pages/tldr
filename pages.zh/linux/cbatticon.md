# cbatticon

> 一个轻量级且快速的电池图标，位于系统托盘中。
> 更多信息：<https://github.com/valr/cbatticon>。

- 在系统托盘中显示电池图标：

`cbatticon`

- 显示电池图标并将更新间隔设置为20秒：

`cbatticon --update-interval {{20}}`

- 列出可用的图标类型：

`cbatticon --list-icon-types`

- 以特定图标类型显示电池图标：

`cbatticon --icon-type {{standard|notification|symbolic}}`

- 列出可用的电源供应：

`cbatticon --list-power-supplies`

- 显示特定电池的电池图标：

`cbatticon {{BAT0}}`

- 显示电池图标并在电池电量达到设定的临界水平时执行指定命令：

`cbatticon --critical-level {{5}} --command-critical-level {{poweroff}}`