# Gammastep

> 根据一天中的时间调整屏幕的色温。
> 更多信息：<https://gitlab.com/chinstrap/gammastep>。

- 在白天（例如5700k）和夜间（例如3600k）以特定的[t]emperature开启Gammastep：

`gammastep -t {{5700}}:{{3600}}`

- 以手动指定的自定义[l]ocation开启Gammastep：

`gammastep -l {{纬度}}:{{经度}}`

- 在白天（例如70%）和夜间（例如40%）以特定的屏幕[b]rightness开启Gammastep，最小亮度10%，最大亮度100%：

`gammastep -b {{0.7}}:{{0.4}}`

- 以自定义[g]amma等级（在0到1之间）开启Gammastep：

`gammastep -g {{红}}:{{绿}}:{{蓝}}`

- 以不变的恒定色温[c]onstant开启Gammastep：

`gammastep -O {{温度}}`

- 重置Gammastep应用的温度调整：

`gammastep -x`