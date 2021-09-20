# systeminfo

> 显示本地或远程计算机的操作系统配置。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- 显示本地计算机的操作系统配置：

`systeminfo`

- 以指定的输出格式显示系统配置：

`systeminfo /fo {{table|list|csv}}`

- 显示远程计算机的系统配置：

`systeminfo /s {{远程主机名}} /u {{用户名}} /p {{密码}}`

- 显示详细的帮助信息：

`systeminfo /?`
