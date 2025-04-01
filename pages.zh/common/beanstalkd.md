# beanstalkd

> 一个简单且通用的工作队列服务器。
> 更多信息：<https://manned.org/beanstalkd>.

- 启动服务器，监听 11300 端口：

`beanstalkd`

- 监听特定的 [p]ort 和地址：

`beanstalkd -l {{ip_address}} -p {{port_number}}`

- 通过保存到磁盘来持久化工作队列：

`beanstalkd -b {{path/to/persistence_directory}}`

- 每 500 毫秒同步一次到持久化目录：

`beanstalkd -b {{path/to/persistence_directory}} -f {{500}}`