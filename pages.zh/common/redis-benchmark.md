# redis-benchmark

> 基准测试 Redis 服务器。
> 更多信息：<https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/>.

- 运行完整基准测试：

`redis-benchmark`

- 在特定的 Redis 服务器上运行基准测试：

`redis-benchmark -h {{host}} -p {{port}} -a {{password}}`

- 运行默认 100000 请求的子集测试：

`redis-benchmark -h {{host}} -p {{port}} -t {{set,lpush}} -n {{100000}}`

- 使用特定脚本运行测试：

`redis-benchmark -n {{100000}} script load "{{redis.call('set', 'foo', 'bar')}}"`

- 使用 100000 个 [r]andom 键运行基准测试：

`redis-benchmark -t {{set}} -r {{100000}}`

- 使用 16 个命令的 [P]ipelining 运行基准测试：

`redis-benchmark -n {{1000000}} -t {{set,get}} -P {{16}}`

- 安静地运行基准测试并仅显示每秒查询结果：

`redis-benchmark -q`