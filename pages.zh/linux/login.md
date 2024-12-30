# 登录

> 为用户启动一个会话。
> 更多信息：<https://manned.org/login>。

- 作为用户登录：

`login {{user}}`

- 如果用户已预认证，则无需身份验证登录：

`login -f {{user}}`

- 作为用户登录并保留环境：

`login -p {{user}}`

- 在远程主机上作为用户登录：

`login -h {{host}} {{user}}`