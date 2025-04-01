# auditctl

> 用于控制 Linux 审计系统的功能、获取状态和管理规则。
> 更多信息：<https://manned.org/auditctl>.

- 显示审计系统的[状态]：

`sudo auditctl -s`

- [列出]所有当前加载的审计规则：

`sudo auditctl -l`

- [删除]所有审计规则：

`sudo auditctl -D`

- [启用/禁用]审计系统：

`sudo auditctl -e {{1|0}}`

- 监视文件的更改：

`sudo auditctl -a always,exit -F arch=b64 -F path={{/path/to/file}} -F perm=wa`

- 递归监视目录的更改：

`sudo auditctl -a always,exit -F arch=b64 -F dir={{/path/to/directory/}} -F perm=wa`

- 显示[帮助]：

`auditctl -h`