# redshift

> 根据周围环境调整屏幕的色温。
> 更多信息：<https://manned.org/redshift>.

- 使用特定的白天（例如，5700K）和夜晚（例如，3600K）[t]色温启动 Redshift：

`redshift -t {{5700}}:{{3600}}`

- 使用手动指定的自定义[l]位置启动 Redshift：

`redshift -l {{纬度}}:{{经度}}`

- 使用特定的白天（例如，70%）和夜晚（例如，40%）[b]屏幕亮度启动 Redshift：

`redshift -b {{0.7}}:{{0.4}}`

- 使用自定义[g]伽玛值（0 到 1 之间）启动 Redshift：

`redshift -g {{red}}:{{green}}:{{blue}}`

- 在 [O]一次性模式中[p]清除现有色温变化并设置恒定的不变色温：

`redshift -PO {{色温}}`