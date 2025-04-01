# htpdate

> 通过从 Web 服务器获取 HTTP 头来同步本地日期和时间。
> 更多信息：<https://www.vervest.org/htp/>。

- 同步日期和时间：

`sudo htpdate {{host}}`

- 模拟同步过程，但不执行任何实际操作：

`htpdate -q {{host}}`

- 补偿系统时钟偏差：

`sudo htpdate -x {{host}}`

- 同步后立即设置时间：

`sudo htpdate -s {{host}}`