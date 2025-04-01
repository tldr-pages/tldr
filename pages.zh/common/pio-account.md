# pio account

> 在命令行中管理您的 PlatformIO 账户。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/account/>.

- 注册一个新的 PlatformIO 账户：

`pio account register --username {{username}} --email {{email}} --password {{password}} --firstname {{firstname}} --lastname {{lastname}}`

- 永久删除您的 PlatformIO 账户和相关数据：

`pio account destroy`

- 登录您的 PlatformIO 账户：

`pio account login --username {{username}} --password {{password}}`

- 注销您的 PlatformIO 账户：

`pio account logout`

- 更新您的 PlatformIO 个人资料：

`pio account update --username {{username}} --email {{email}} --firstname {{firstname}} --lastname {{lastname}} --current-password {{password}}`

- 显示有关您的 PlatformIO 账户的详细信息：

`pio account show`

- 使用您的用户名或邮箱重置密码：

`pio account forgot --username {{username_or_email}}`