# docker login

> 登录 Docker 注册表。
> 更多信息：<https://docs.docker.com/reference/cli/docker/login/>.

- 交互式登录到注册表：

`docker login`

- 使用特定用户名登录到注册表（用户将被提示输入密码）：

`docker login --username {{username}}`

- 使用用户名和密码登录到注册表：

`docker login --username {{username}} --password {{password}} {{server}}`

- 使用从 `stdin` 输入的密码登录到注册表：

`echo "{{password}}" | docker login --username {{username}} --password-stdin`
