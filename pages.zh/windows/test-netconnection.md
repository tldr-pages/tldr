# Test-NetConnection

> 显示连接的诊断信息。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection>.

- 测试连接并显示详细结果：

`Test-NetConnection -InformationLevel Detailed`

- 使用指定的端口号测试与远程主机的连接：

`Test-NetConnection -ComputerName {{ip_or_hostname}} -Port {{port_number}}`