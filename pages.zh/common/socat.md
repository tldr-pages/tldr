# socat

> 多用途中继（SOcket CAT）。
> 更多信息：<http://www.dest-unreach.org/socat/>.

- 监听一个端口，等待传入连接并将数据转移到STDIO：

`sudo socat - TCP-LISTEN:8080,fork`

- 使用SSL监听一个端口并打印到STDOUT：

`sudo socat OPENSSL-LISTEN:4433,reuseaddr,cert=./cert.pem,cafile=./ca.cert.pem,key=./key.pem,verify=0 STDOUT`

- 创建到主机和端口的连接，将STDIO中的数据传输到连接的主机：

`sudo socat - TCP4:www.example.com:80`

- 将本地端口的传入数据转发到另一个主机和端口：

`sudo socat TCP-LISTEN:80,fork TCP4:www.example.com:80`