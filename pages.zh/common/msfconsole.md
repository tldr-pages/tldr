# msfconsole

> Metasploit框架的控制台。
> 更多信息请访问：<https://docs.rapid7.com/metasploit/msf-overview>。

- 启动控制台：

`msfconsole`

- 安静地启动控制台，不显示任何横幅：

`msfconsole --quiet`

- 不启用数据库支持：

`msfconsole --no-database`

- 执行控制台命令（注意：使用 `;` 来传递多个命令）：

`msfconsole --execute-command "{{use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run}}"`

- 显示版本：

`msfconsole --version`