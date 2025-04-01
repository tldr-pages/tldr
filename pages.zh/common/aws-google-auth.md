# aws-google-auth

> 使用 Google Apps 作为联合（单点登录）提供者获取 AWS 临时（STS）凭证。
> 更多信息：<https://github.com/cevoaustralia/aws-google-auth>.

- 使用指定的用户名、IDP 和 SP 标识符通过 Google SSO 登录，并将凭证的有效期设置为一小时：

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}}`

- 登录时询问使用哪个角色（如果有多个可用的 SAML 角色）：

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}}`

- 解析 AWS 账户的别名：

`aws-google-auth {{[-u|--username]}} {{example@example.com}} {{[-I|--idp-id]}} {{$GOOGLE_IDP_ID}} {{[-S|--sp-id]}} {{$GOOGLE_SP_ID}} {{[-d|--duration]}} {{3600}} {{[-a|--ask-role]}} --resolve-aliases`

- 显示帮助：

`aws-google-auth {{[-h|--help]}}`
