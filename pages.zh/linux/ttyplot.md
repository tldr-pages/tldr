# ttyplot

> 一个用于命令行的实时绘图工具，数据输入来自 `stdin`。
> 更多信息：<https://github.com/tenox7/ttyplot>。

- 绘制值 `1`、`2` 和 `3`（`cat` 防止 ttyplot 退出）：

`{ echo {{1 2 3}}; cat } | ttyplot`

- 设置特定的标题和单位：

`{ echo {{1 2 3}}; cat } | ttyplot -t {{title}} -u {{unit}}`

- 使用 while 循环连续绘制随机值：

`{ while {{true}}; do echo {{$RANDOM}}; sleep {{1}}; done } | ttyplot`

- 解析 `ping` 的输出并可视化：

`ping {{8.8.8.8}} | sed -u '{{s/^.*time=//g; s/ ms//g}}' | ttyplot -t "{{ping to 8.8.8.8}}" -u {{ms}}`
