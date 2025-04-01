# ssh-keygen

> 生成用于身份验证、免密码登录等的 SSH 密钥。
> 更多信息：<https://man.openbsd.org/ssh-keygen>.

- 交互式生成密钥：

`ssh-keygen`

- 生成 ed25519 密钥，使用 32 次密钥派生函数迭代并保存密钥到指定文件：

`ssh-keygen -t {{ed25519}} -a {{32}} -f {{~/.ssh/filename}}`

- 生成 4096 位的 RSA 密钥，包含电子邮件作为注释：

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{comment|email}}"`

- 从 known_hosts 文件中移除主机的密钥（在已知主机有新密钥时非常有用）：

`ssh-keygen -R {{remote_host}}`

- 获取密钥的 MD5 十六进制指纹：

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/filename}}`

- 更改密钥的密码：

`ssh-keygen -p -f {{~/.ssh/filename}}`

- 更改密钥格式类型（例如从 OPENSSH 格式转换为 PEM），文件将就地重写：

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/OpenSSH_private_key}}`

- 从私钥中提取公钥：

`ssh-keygen -y -f {{~/.ssh/OpenSSH_private_key}}`
