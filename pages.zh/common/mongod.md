# mongod

> MongoDB 数据库服务器。
> 更多信息：<https://docs.mongodb.com/manual/reference/program/mongod>.

- 指定配置文件：

`mongod --config {{filename}}`

- 指定要监听的端口：

`mongod --port {{port}}`

- 指定数据库分析级别，用于性能调优分析。 0 - 关闭，1 - 仅是记录慢速操作，2 - 全部：

`mongod --profile {{0|1|2}}`
