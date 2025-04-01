# hydra

> 在线密码猜测工具。
> 支持的协议包括 FTP、HTTP(S)、SMTP、SNMP、XMPP、SSH 等。
> 更多信息：<https://github.com/vanhauser-thc/thc-hydra>。

- 启动 Hydra 的向导：

`hydra-wizard`

- 使用指定的用户名和密码列表猜测 SSH 凭据：

`hydra -l {{username}} -P {{path/to/wordlist.txt}} {{host_ip}} {{ssh}}`

- 使用两个特定的用户名和密码列表猜测 HTTPS 表单凭据（"https_post_request" 可以是 "username=^USER^&password=^PASS^"）：

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} {{host_ip}} {{https-post-form}} "{{url_without_host}}:{{https_post_request}}:{{login_failed_string}}"`

- 使用用户名和密码列表猜测 FTP 凭据，并指定线程数：

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -t {{n_tasks}} {{host_ip}} {{ftp}}`

- 使用用户名和密码列表猜测 MySQL 凭据，找到用户名/密码组合后退出：

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -f {{host_ip}} {{mysql}}`

- 使用用户名和密码列表猜测 RDP 凭据，并显示每次尝试：

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -V {{rdp://host_ip}}`

- 在一系列主机上使用冒号分隔的用户名/密码对列表猜测 IMAP 凭据：

`hydra -C {{path/to/username_password_pairs.txt}} {{imap://[host_range_cidr]}}`

- 使用用户名和密码列表在主机列表上猜测 POP3 凭据，找到用户名/密码组合后退出：

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -M {{path/to/hosts.txt}} -F {{pop3}}`
