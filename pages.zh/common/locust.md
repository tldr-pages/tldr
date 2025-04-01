# locust

> 负载测试工具，用于确定系统可以处理的并发用户数。
> 更多信息：<https://locust.io>.

- 使用 locustfile.py 对 "example.com" 进行负载测试，并使用 Web 界面：

`locust --host={{http://example.com}}`

- 使用不同的测试文件：

`locust --locustfile={{test_file.py}} --host={{http://example.com}}`

- 不使用 Web 界面运行测试，每秒生成 1 个用户，直到有 100 个用户：

`locust --no-web --clients={{100}} --hatch-rate={{1}} --host={{http://example.com}}`

- 以主节点模式启动 Locust：

`locust --master --host={{http://example.com}}`

- 连接从节点到主节点：

`locust --slave --host={{http://example.com}}`

- 连接从节点到不同机器上的主节点：

`locust --slave --master-host={{master_hostname}} --host={{http://example.com}}`
