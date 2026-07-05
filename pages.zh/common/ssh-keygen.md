# ssh-keygen

> 生成用于身份验证、免密码登录和其他用途的 SSH 密钥。
> 另请参阅：`ssh-copy-id`。
> 更多信息：<https://man.openbsd.org/ssh-keygen>。

- 以交互方式生成密钥：

`ssh-keygen`

- 生成 ed25519 密钥，使用 32 轮密钥派生函数，并保存到指定文件：

`ssh-keygen -f {{~/.ssh/文件名}} -t ed25519 -a 32`

- 生成 4096 位 RSA 密钥，并使用电子邮件作为注释：

`ssh-keygen -t rsa -b 4096 -C "{{注释|电子邮件}}"`

- 从 `known_hosts` 文件中移除某个主机的密钥（当已知主机有新密钥时很有用）：

`ssh-keygen -R {{远程主机}}`

- 以 MD5 十六进制格式获取密钥指纹：

`ssh-keygen -f {{~/.ssh/文件名}} -l -E md5`

- 更改密钥的密码：

`ssh-keygen -f {{~/.ssh/文件名}} -p`

- 更改密钥格式类型（例如从 OPENSSH 格式更改为 PEM），文件将被就地重写：

`ssh-keygen -f {{~/.ssh/OpenSSH_私钥}} -p -m PEM`

- 从私钥中获取公钥：

`ssh-keygen -f {{~/.ssh/OpenSSH_私钥}} -y`
