# gh auth

> 使用 GitHub 主机进行身份验证。
> 更多信息：<https://cli.github.com/manual/gh_auth>。

- 使用交互提示登录：

`gh auth login`

- 使用来自 `stdin` 的令牌登录（在 <https://github.com/settings/tokens> 创建）：

`echo {{your_token}} | gh auth login --with-token`

- 检查您是否已登录：

`gh auth status`

- 登出：

`gh auth logout`

- 使用特定的 GitHub 企业服务器登录：

`gh auth login --hostname {{github.example.com}}`

- 刷新会话以确保身份验证凭据具有正确的最低作用域（移除之前请求的附加作用域）：

`gh auth refresh`

- 扩展权限作用域：

`gh auth refresh --scopes {{repo,admin:repo_hook,admin:org,admin:public_key,admin:org_hook,...}}`