# psexec

> 在远程计算机上执行命令行进程。
> 这是一个高级命令，可能具有潜在危险。
> 更多信息：<https://learn.microsoft.com/sysinternals/downloads/psexec>。

- 使用 `cmd` 在远程 shell 中执行命令：

`psexec \\{{remote_host}} cmd`

- 在已预先认证的远程主机上执行命令：

`psexec \\{{remote_host}} -u {{user_name}} -p {{password}}`

- 远程执行命令并将结果输出到文件：

`psexec \\{{remote_host}} cmd /c {{command}} -an ^>{{path\to\file.txt}}`

- 远程执行可与用户交互的程序：

`psexec \\{{remote_host}} -d -i {{program_name}}`

- 显示远程主机的 IP 配置：

`psexec \\{{remote_host}} ipconfig /all`
