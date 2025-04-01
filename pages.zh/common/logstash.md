# logstash

> 一个 Elasticsearch ETL（提取、转换和加载）工具。
> 常用于从各种数据源（如数据库和日志文件）加载数据到 Elasticsearch 中。
> 更多信息：<https://www.elastic.co/products/logstash>。

- 检查 Logstash 配置的有效性：

`logstash --configtest --config {{logstash_config.conf}}`

- 使用配置文件运行 Logstash：

`sudo logstash --config {{logstash_config.conf}}`

- 使用最简单的内联配置字符串运行 Logstash：

`sudo logstash -e 'input {} filter {} output {}'`