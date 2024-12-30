# hydra

> 在线密码猜测工具。
> 支持的协议包括 FTP、HTTP(S)、SMTP、SNMP、XMPP、SSH 等。
> 更多信息：<https://github.com/vanhauser-thc/thc-hydra>。

- 启动 Hydra 向导：

`hydra-wizard`

- 使用给定的用户名和密码列表猜测 SSH 凭证：

`hydra -l {{username}} -P {{path/to/wordlist.txt}} {{host_ip}} {{ssh}}`

- 使用两个特定的用户名和密码列表猜测 HTTPS 网页表单凭证（“https_post_request” 可以是 “username=^USER^&password=^PASS^”）：

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} {{host_ip}} {{https-post-form}} "{{url_without_host}}:{{https_post_request}}:{{login_failed_string}}"`

- 使用用户名和密码列表猜测 FTP 凭证，并指定线程数量：

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -t {{n_tasks}} {{host_ip}} {{ftp}}`

- 使用用户名和密码列表猜测 MySQL 凭证，当找到用户名/密码对时退出：

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -f {{host_ip}} {{mysql}}`

- 使用用户名和密码列表猜测 RDP 凭证，显示每次尝试：

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -V {{rdp://host_ip}}`

- 使用冒号分隔的用户名/密码对列表在一系列主机上猜测 IMAP 凭证：

`hydra -C {{path/to/username_password_pairs.txt}} {{imap://[host_range_cidr]}}`

- 使用用户名和密码列表在一系列主机上猜测 POP3 凭证，当找到用户名/密码对时退出：

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -M {{path/to/hosts.txt}} -F {{pop3}}`