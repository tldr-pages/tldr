# locust

> 负载测试工具，确定系统可以处理的并发用户数量。
> 更多信息：<https://locust.io>。

- 使用 locustfile.py 和 Web 界面对 "example.com" 进行负载测试：

`locust --host={{http://example.com}}`

- 使用不同的测试文件：

`locust --locustfile={{test_file.py}} --host={{http://example.com}}`

- 在没有 Web 界面的情况下运行测试，每秒产生 1 个用户，直到达到 100 个用户：

`locust --no-web --clients={{100}} --hatch-rate={{1}} --host={{http://example.com}}`

- 以主模式启动 Locust：

`locust --master --host={{http://example.com}}`

- 将 Locust 从机连接到主机：

`locust --slave --host={{http://example.com}}`

- 在不同的机器上将 Locust 从机连接到主机：

`locust --slave --master-host={{master_hostname}} --host={{http://example.com}}`