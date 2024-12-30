# authconfig

> 配置系统身份验证资源。
> 更多信息：<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>。

- 显示当前配置（或干运行）：

`authconfig --test`

- 配置服务器使用不同的密码哈希算法：

`authconfig --update --passalgo={{algorithm}}`

- 启用 LDAP 身份验证：

`authconfig --update --enableldapauth`

- 禁用 LDAP 身份验证：

`authconfig --update --disableldapauth`

- 启用网络信息服务（NIS）：

`authconfig --update --enablenis`

- 启用 Kerberos：

`authconfig --update --enablekrb5`

- 启用 Winbind（活动目录）身份验证：

`authconfig --update --enablewinbindauth`

- 启用本地授权：

`authconfig --update --enablelocauthorize`