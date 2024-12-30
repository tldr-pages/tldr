# certutil

> 管理 NSS 数据库和其他 NSS 令牌中的密钥和证书。
> 更多信息：<https://manned.org/certutil>。

- 在当前 [d] 目录中创建一个 [N] 新的证书数据库：

`certutil -N -d .`

- 列出数据库中的所有证书：

`certutil -L -d .`

- 列出数据库中的所有私钥，并指定密码 [f] 文件：

`certutil -K -d . -f {{path/to/password_file.txt}}`

- 将签名证书添加到请求者的数据库中，指定一个 [n] ickname、[t]rust 属性和一个 [i]nput CRT 文件：

`certutil -A -n "{{server_certificate}}" -t ",," -i {{path/to/file.crt}} -d .`

- 使用特定的密钥大小 ([g]) 向给定 [c] 证书添加主题备用名称：

`certutil -S -f {{path/to/password_file.txt}} -d . -t ",," -c "{{server_certificate}}" -n "{{server_name}}" -g {{2048}} -s "CN={{common_name}},O={{organization}}"`