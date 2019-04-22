# ab

> Apache基准测试工具.最简单的压力测试工具.

- 向目标URL执行100次HTTP GET请求:

`ab -n {{100}} {{url}}`

- 使用10个并发请求，同时向目标URL执行100次HTTP GET请求:

`ab -n {{100}} -c {{10}} {{url}}`

- 使用 keep alive:

`ab -k {{url}}`

- 为基准测试设置最大的测试时间(单位: 秒):

`ab -t {{60}} {{url}}`
