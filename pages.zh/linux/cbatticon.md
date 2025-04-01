# cbatticon

> 一个轻量级且快速的电池图标，显示在系统托盘中。
> 更多信息：<https://github.com/valr/cbatticon>.

- 在系统托盘中显示电池图标：

`cbatticon`

- 显示电池图标并设置更新间隔为20秒：

`cbatticon --update-interval {{20}}`

- 列出可用的图标类型：

`cbatticon --list-icon-types`

- 使用特定图标类型显示电池图标：

`cbatticon --icon-type {{standard|notification|symbolic}}`

- 列出可用的电源：

`cbatticon --list-power-supplies`

- 为特定电池显示电池图标：

`cbatticon {{BAT0}}`

- 显示电池图标，并在电池电量达到设定的临界值时执行的命令：

`cbatticon --critical-level {{5}} --command-critical-level {{poweroff}}`