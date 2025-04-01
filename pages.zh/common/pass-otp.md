# pass otp

> 一个用于管理一次性密码（OTP）令牌的 pass 扩展。
> 更多信息：<https://github.com/tadfisher/pass-otp#readme>。

- 提示输入 otpauth URI 令牌并创建一个新的 pass 文件：

`pass otp insert {{path/to/pass}}`

- 提示输入 otpauth URI 令牌并附加到现有的 pass 文件：

`pass otp append {{path/to/pass}}`

- 使用 pass 文件中的 OTP 令牌打印 2FA 代码：

`pass otp {{path/to/pass}}`

- 使用 pass 文件中的 OTP 令牌复制 2FA 代码但不打印：

`pass otp --clip {{path/to/pass}}`

- 使用 pass 文件中存储的 OTP 令牌显示 QR 码：

`pass otp uri --qrcode {{path/to/pass}}`

- 提示输入 OTP 密钥值并指定发件人和账户（至少需要指定一个）并附加到现有的 pass 文件：

`pass otp append --secret --issuer {{issuer_name}} --account {{account_name}} {{path/to/pass}}`