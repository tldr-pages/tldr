# httping

> 测量网页服务器的延迟和吞吐量。
> 更多信息：<https://manned.org/httping>。

- Ping指定的URL：

`httping -g {{url}}`

- Ping指定`host`和`port`上的网页服务器：

`httping -h {{host}} -p {{port}}`

- 使用TLS连接Ping指定`host`上的网页服务器：

`httping -l -g https://{{host}}`

- 使用HTTP基本认证Ping指定`host`上的网页服务器：

`httping -g http://{{host}} -U {{username}} -P {{password}}`