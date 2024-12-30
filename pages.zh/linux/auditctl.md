# auditctl

> 控制Linux审计系统的行为、获取状态和管理规则的工具。
> 更多信息：<https://manned.org/auditctl>。

- 显示审计系统的[s]tatus：

`sudo auditctl -s`

- [l]ist当前加载的所有审计规则：

`sudo auditctl -l`

- [D]elete所有审计规则：

`sudo auditctl -D`

- [e]nable/disable审计系统：

`sudo auditctl -e {{1|0}}`

- 监视文件的变化：

`sudo auditctl -a always,exit -F arch=b64 -F path={{/path/to/file}} -F perm=wa`

- 递归监视目录的变化：

`sudo auditctl -a always,exit -F arch=b64 -F dir={{/path/to/directory/}} -F perm=wa`

- 显示[h]elp：

`auditctl -h`