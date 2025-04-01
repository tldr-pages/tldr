# certutil

> 管理 NSS 数据库和其他 NSS 令牌中的密钥和证书。
> 更多信息：<https://manned.org/certutil>.

- 在当前目录中创建一个新 [N] 证书数据库：

`certutil -N -d .`

- 列出数据库中的所有证书：

`certutil -L -d .`

- 列出数据库中的所有私钥，指定密码文件 [f]：

`certutil -K -d . -f {{path/to/password_file.txt}}`

- 将签名证书添加到请求者的数据库中，指定别名 [n]、信任属性 [t] 和输入 CRT 文件 [i]：

`certutil -A -n "{{server_certificate}}" -t ",," -i {{path/to/file.crt}} -d .`

- 使用特定密钥大小 [g] 为指定证书 [c] 添加主题备用名称：

`certutil -S -f {{path/to/password_file.txt}} -d . -t ",," -c "{{server_certificate}}" -n "{{server_name}}" -g {{2048}} -s "CN={{common_name}},O={{organization}}"`