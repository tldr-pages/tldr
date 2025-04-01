# rsstail

> 用于 RSS 源的 `tail` 工具。
> 更多信息：<https://github.com/gvalkov/rsstail.py>。

- 显示给定 URL 的源并等待新条目出现在底部：

`rsstail -u {{url}}`

- 以倒序时间顺序显示源（新条目在底部）：

`rsstail -r -u {{url}}`

- 包括发布日期和链接：

`rsstail -pl -u {{url}}`

- 设置更新间隔：

`rsstail -u {{url}} -i {{interval_in_seconds}}`

- 显示源并退出：

`rsstail -1 -u {{url}}`
