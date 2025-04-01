# nikto

> Web 服务器扫描工具，可对 Web 服务器进行多方面的测试。
> 更多信息：<https://cirt.net/Nikto2>.

- 对目标主机执行基本的 Nikto 扫描：

`perl nikto.pl -h {{192.168.0.1}}`

- 在执行基本扫描时指定端口号：

`perl nikto.pl -h {{192.168.0.1}} -p {{443}}`

- 使用完整的 URL 语法扫描端口和协议：

`perl nikto.pl -h {{https://192.168.0.1:443/}}`

- 在同一扫描会话中扫描多个端口：

`perl nikto.pl -h {{192.168.0.1}} -p {{80,88,443}}`

- 更新到最新的插件和数据库：

`perl nikto.pl -update`