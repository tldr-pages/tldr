# glab auth

> 使用 GitLab 主机进行身份验证。
> 更多信息：<https://glab.readthedocs.io/en/latest/auth>.

- 使用交互提示登录：

`glab auth login`

- 使用令牌登录：

`glab auth login --token {{token}}`

- 检查身份验证状态：

`glab auth status`

- 登录到特定的 GitLab 实例：

`glab auth login --hostname {{gitlab.example.com}}`