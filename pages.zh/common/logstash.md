# logstash

> 一个Elasticsearch的ETL（提取、转换和加载）工具。
> 通常用于将各种来源（如数据库和日志文件）中的数据加载到Elasticsearch中。
> 更多信息：<https://www.elastic.co/products/logstash>。

- 检查Logstash配置的有效性：

`logstash --configtest --config {{logstash_config.conf}}`

- 使用配置运行Logstash：

`sudo logstash --config {{logstash_config.conf}}`

- 使用最基本的内联配置字符串运行Logstash：

`sudo logstash -e 'input {} filter {} output {}'`