# ansiweather

> 在你的终端中显示当前天气状况。
> 更多信息：<https://github.com/fcambus/ansiweather>。

- 使用公制单位显示特定地点接下来七天的天气预报：

`ansiweather -u metric -f 7 -l {{Rzeszow,PL}}`

- 显示接下来五天的天气预报，包含符号和白天数据，针对你当前的位置：

`ansiweather -F -s true -d true`

- 显示你当前地点的今天的风速和湿度数据：

`ansiweather -w true -h true`