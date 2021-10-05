# ansiweather

> 一个 shell 脚本，用于在终端中显示当前的天气状况。
> 更多信息：<https://github.com/fcambus/ansiweather>.

- 使用公制单位显示 Rzeszow, Poland 接下来 5 天的天气预报：

`ansiweather -u {{metric}} -f {{5}} -l {{Rzeszow,PL}}`

- 显示带符号和日光数据信息的天气预报：

`ansiweather -s {{true}} -d {{true}}`

- 显示带风力等级和湿度信息的天气预报：

`ansiweather -w {{true}} -h {{true}}`
