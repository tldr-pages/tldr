# oathtool

> OATH 一次性密码工具。
> 更多信息: <https://www.nongnu.org/oath-toolkit/oathtool.1.html>。

- 生成 TOTP 令牌（行为类似于 Google Authenticator）：

`oathtool --totp --base32 "{{secret}}"`

- 为特定时间生成 TOTP 令牌：

`oathtool --totp --now "{{2004-02-29 16:21:42}}" --base32 "{{secret}}"`

- 验证 TOTP 令牌：

`oathtool --totp --base32 "{{secret}}" "{{token}}"`