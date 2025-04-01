# msfconsole

> Metasploit 框架的控制台。
> 更多信息：<https://docs.rapid7.com/metasploit/msf-overview>.

- 启动控制台：

`msfconsole`

- 安静模式启动控制台，不显示欢迎信息：

`msfconsole {{[-q|--quiet]}}`

- 不启用数据库支持：

`msfconsole {{[-n|--no-database]}}`

- 执行控制台命令（注意：多个命令用 `;` 分隔）：

`msfconsole {{[-x|--execute-command]}} "{{use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run}}"`

- 显示帮助信息：

`msfconsole {{[-h|--help]}}`

- 显示版本信息：

`msfconsole {{[-v|--version]}}`