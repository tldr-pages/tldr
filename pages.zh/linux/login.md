# login

> 为用户启动会话。
> 更多信息：<https://manned.org/login>.

- 以用户身份登录：

`login {{user}}`

- 如果用户已预先身份验证，则无需身份验证即可登录：

`login -f {{user}}`

- 以用户身份登录并保留环境：

`login -p {{user}}`

- 在远程主机上以用户身份登录：

`login -h {{host}} {{user}}`
