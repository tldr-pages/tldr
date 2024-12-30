# htpdate

> 通过来自网络服务器的HTTP头同步本地日期和时间。
> 更多信息请访问：<https://www.vervest.org/htp/>.

- 同步日期和时间：

`sudo htpdate {{host}}`

- 执行同步的模拟，不采取任何行动：

`htpdate -q {{host}}`

- 补偿系统时钟漂移：

`sudo htpdate -x {{host}}`

- 在同步后立即设置时间：

`sudo htpdate -s {{host}}`