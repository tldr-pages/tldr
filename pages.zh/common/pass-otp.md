# 通行证 OTP

> 用于管理一次性密码 (OTP) 令牌的通行证扩展。
> 更多信息：<https://github.com/tadfisher/pass-otp#readme>。

- 提示输入一个 otpauth URI 令牌并创建一个新的通行证文件：

`pass otp insert {{path/to/pass}}`

- 提示输入一个 otpauth URI 令牌并追加到现有的通行证文件：

`pass otp append {{path/to/pass}}`

- 使用通行证文件中的 OTP 令牌打印 2FA 代码：

`pass otp {{path/to/pass}}`

- 使用通行证文件中的 OTP 令牌复制而不打印 2FA 代码：

`pass otp --clip {{path/to/pass}}`

- 使用存储在通行证文件中的 OTP 令牌显示 QR 码：

`pass otp uri --qrcode {{path/to/pass}}`

- 提示输入一个 OTP 密钥值，指定发行者和账户（至少需要指定一个），并追加到现有的通行证文件：

`pass otp append --secret --issuer {{issuer_name}} --account {{account_name}} {{path/to/pass}}`