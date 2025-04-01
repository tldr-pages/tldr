# influx

> InfluxDB 命令行客户端。
> 更多信息：<https://docs.influxdata.com/influxdb/v1.7/tools/shell/>。

- 连接到本地不使用凭据的 InfluxDB：

`influx`

- 使用特定用户名连接（将提示输入密码）：

`influx -username {{username}} -password ""`

- 连接到特定主机：

`influx -host {{hostname}}`

- 使用特定数据库：

`influx -database {{database_name}}`

- 执行给定的命令：

`influx -execute "{{influxql_command}}"`

- 以特定格式返回输出：

`influx -execute "{{influxql_command}}" -format {{json|csv|column}}`
