# gh auth

> 与 GitHub 主机进行身份验证。
> 更多信息：<https://cli.github.com/manual/gh_auth>。

- 使用交互式提示登录：

`gh auth login`

- 使用从 `stdin` 输入的令牌登录（令牌在 <https://github.com/settings/tokens> 创建）：

`echo {{your_token}} | gh auth login --with-token`

- 检查是否已登录：

`gh auth status`

- 注销：

`gh auth logout`

- 与特定的 GitHub Enterprise Server 登录：

`gh auth login --hostname {{github.example.com}}`

- 刷新会话以确保身份验证凭据具有正确的最小权限范围（移除之前请求的额外权限范围）：

`gh auth refresh`

- 扩展权限范围：

`gh auth refresh --scopes {{repo,admin:repo_hook,admin:org,admin:public_key,admin:org_hook,...}}`
