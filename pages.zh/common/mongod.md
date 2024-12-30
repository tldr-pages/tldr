# mongod

> MongoDB 数据库服务器。
> 更多信息请访问：<https://docs.mongodb.com/manual/reference/program/mongod>。

- 指定存储目录（默认：Linux 和 macOS 上为 `/data/db`，Windows 上为 `C:\data\db`）：

`mongod --dbpath {{path/to/directory}}`

- 指定配置文件：

`mongod --config {{path/to/file}}`

- 指定监听的端口（默认：27017）：

`mongod --port {{port}}`

- 指定数据库分析级别。0 关闭，1 仅慢操作，2 所有（默认：0）：

`mongod --profile {{0|1|2}}`