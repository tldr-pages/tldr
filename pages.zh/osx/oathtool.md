# oathtool

> OATH 一次性密码工具。

- 生成 TOTP 令牌（行为类似于 Google Authenticator）：

`oathtool --totp --base32 {{密码}}`

- 根据给定时间产生特定的 TOTP 令牌：

`oathtool --totp --now {{2004-02-29 16:21:42}} --base32 {{密码}}`

- 验证 TOTP 令牌：

`oathtool --totp --base32 {{密码}} {{令牌}}`
