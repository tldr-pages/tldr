# gh auth

> 进行 GitHub 主机的身份验证。
> 更多信息：<https://cli.github.com/manual/gh_auth>。

- 通过交互式提示进行登录：

`gh auth login`

- 使用来自 `stdin` 的令牌进行登录（在 <https://github.com/settings/tokens> 创建）：

`echo {{你的令牌}} | gh auth login --with-token`

- 检查当前登录状态：

`gh auth status`

- 登出当前账户：

`gh auth logout`

- 登录指定的 GitHub 企业版服务器：

`gh auth login {{[-h|--hostname]}} {{github.example.com}}`

- 刷新身份验证凭据，并恢复为默认的最小权限范围（移除之前额外申请的权限）：

`gh auth refresh`

- 扩展当前权限范围：

`gh auth refresh {{[-s|--scopes]}} {{repo,admin:repo_hook,admin:org,admin:public_key,admin:org_hook,...}}`
