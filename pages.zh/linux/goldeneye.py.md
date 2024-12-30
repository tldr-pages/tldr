# goldeneye.py

> 一款 HTTP DoS 测试工具。
> 更多信息请访问: <https://github.com/jseidl/GoldenEye>。

- 测试特定网站：

`./goldeneye.py {{url}}`

- 使用 100 个用户代理和 200 个并发套接字测试特定网站：

`./goldeneye.py {{url}} --useragents 100 --sockets 200`

- 测试特定网站时不验证 SSL 证书：

`./goldeneye.py {{url}} --nosslcheck`

- 以调试模式测试特定网站：

`./goldeneye.py {{url}} --debug`

- 显示帮助信息：

`./goldeneye.py --help`