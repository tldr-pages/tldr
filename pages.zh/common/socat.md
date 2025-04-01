# socat

> 多功能中继（SOcket CAT）。
> 更多信息：<http://www.dest-unreach.org/socat/>.

- 监听端口，等待传入连接并将数据传输到 STDIO：

`sudo socat - TCP-LISTEN:8080,fork`

- 使用 SSL 监听端口并将数据打印到 STDOUT：

`sudo socat OPENSSL-LISTEN:4433,reuseaddr,cert=./cert.pem,cafile=./ca.cert.pem,key=./key.pem,verify=0 STDOUT`

- 连接到主机和端口，将 STDIO 中的数据传输到已连接的主机：

`sudo socat - TCP4:www.example.com:80`

- 将本地端口的传入数据转发到另一个主机和端口：

`sudo socat TCP-LISTEN:80,fork TCP4:www.example.com:80`

- 使用多播路由方案发送数据：

`{{echo "Hello Multicast"}} | socat - UDP4-DATAGRAM:{{224.0.0.1}}:{{5000}}`

- 从多播接收数据：

`socat - UDP4-RECVFROM:{{5000}}`