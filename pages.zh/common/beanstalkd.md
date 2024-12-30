# beanstalkd

> 一个简单通用的工作队列服务器。
> 更多信息：<https://beanstalkd.github.io/>.

- 启动服务器，监听11300端口：

`beanstalkd`

- 在特定的[p]ort和地址上监听：

`beanstalkd -l {{ip_address}} -p {{port_number}}`

- 通过将工作队列保存到磁盘来持久化：

`beanstalkd -b {{path/to/persistence_directory}}`

- 每500毫秒同步到持久化目录：

`beanstalkd -b {{path/to/persistence_directory}} -f {{500}}`