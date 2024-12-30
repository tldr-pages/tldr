# aws-google-auth

> 使用 Google 应用作为联合（单点登录）提供者获取 AWS 临时（STS）凭证。
> 更多信息：<https://github.com/cevoaustralia/aws-google-auth>。

- 使用指定的 [u] 用户名 [I] DP 和 [S] P 标识符通过 Google SSO 登录，并将凭证 [d] 持续时间设置为一个小时：

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- 登录时 [a] 询问使用哪个角色（在有多个可用 SAML 角色的情况下）：

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- 解析 AWS 账户的别名：

`aws-google-auth -u {{example@example.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- 显示帮助信息：

`aws-google-auth -h`