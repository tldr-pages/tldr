# ssh-keygen

> 生成用于身份验证、无密码登录和其他用途的 SSH 密钥。
> 更多信息：<https://man.openbsd.org/ssh-keygen>。

- 交互式生成密钥：

`ssh-keygen`

- 生成一个 ed25519 密钥，使用 32 次密钥派生函数，并将密钥保存到指定文件：

`ssh-keygen -t {{ed25519}} -a {{32}} -f {{~/.ssh/filename}}`

- 生成一个 4096 位的 RSA 密钥，并将电子邮件作为注释：

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{comment|email}}"`

- 从 known_hosts 文件中移除一个主机的密钥（当已知主机有新密钥时很有用）：

`ssh-keygen -R {{remote_host}}`

- 以 MD5 十六进制格式检索密钥的指纹：

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/filename}}`

- 修改密钥的密码：

`ssh-keygen -p -f {{~/.ssh/filename}}`

- 更改密钥格式的类型（例如从 OPENSSH 格式到 PEM），文件将原地重写：

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/OpenSSH_private_key}}`

- 从私钥中检索公钥：

`ssh-keygen -y -f {{~/.ssh/OpenSSH_private_key}}`