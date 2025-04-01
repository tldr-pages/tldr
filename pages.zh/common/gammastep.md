# Gammastep

> 根据一天中的时间调整屏幕的色温。
> 更多信息：<https://gitlab.com/chinstrap/gammastep>.

- 以特定的 [t]emperature（例如：5700K）在白天和夜晚（例如：3600K）启动 Gammastep：

`gammastep -t {{5700}}:{{3600}}`

- 以手动指定的自定义 [l]ocation 启动 Gammastep：

`gammastep -l {{latitude}}:{{longitude}}`

- 以特定的 [b]rightness（例如：白天70%，夜晚40%），最小亮度10%，最大亮度100%启动 Gammastep：

`gammastep -b {{0.7}}:{{0.4}}`

- 以自定义的 [g]amma 级别（0到1之间）启动 Gammastep：

`gammastep -g {{red}}:{{green}}:{{blue}}`

- 以恒定不变的色温启动 Gammastep：

`gammastep -O {{temperature}}`

- 重置 Gammastep 应用的色温调整：

`gammastep -x`
