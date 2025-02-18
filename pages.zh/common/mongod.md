# mongod

> MongoDB 数据库服务器。
> 更多信息：<https://docs.mongodb.com/manual/reference/program/mongod>.

- 指定存储目录（默认：Linux 和 macOS 为 `/data/db`，Windows 为 `C:\data\db`）：

`mongod --dbpath {{路径/到/目录}}`

- 指定配置文件：

`mongod --config {{路径/到/文件}}`

- 指定监听的端口（默认：27017）：

`mongod --port {{端口}}`

- 指定数据库分析级别。0 为关闭，1 仅慢操作，2 所有（默认：0）：

`mongod --profile {{0|1|2}}`
