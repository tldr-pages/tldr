# authconfig

> 用于设置系统认证资源的命令行界面。
> 更多信息：<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

- 显示当前的配置（或空运行）：

`authconfig --test`

- 设置服务器使用另一种不同的密码散列算法：

`authconfig --update --passalgo={{算法名}}`

- 启用 LDAP 认证：

`authconfig --update --enableldapauth`

- 关闭 LDAP 认证：

`authconfig --update --disableldapauth`

- 开启网络信息服务（NIS）：

`authconfig --update --enablenis`

- 开启 Kerberos:

`authconfig --update --enablekrb5`

- 开启 Winbind（活动目录）认证：

`authconfig --update --enablewinbindauth`

- 开启本地认证：

`authconfig --update --enablelocauthorize`
