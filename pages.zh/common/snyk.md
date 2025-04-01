# snyk

> 在您的代码中查找漏洞并缓解风险。
> 更多信息：<https://snyk.io>.

- 登录您的 Snyk 账户：

`snyk auth`

- 测试您的代码中是否存在已知漏洞：

`snyk test`

- 测试本地 Docker 镜像中是否存在已知漏洞：

`snyk test --docker {{docker_image}}`

- 在 snyk.io 上记录依赖关系和任何漏洞的状态：

`snyk monitor`

- 自动修补和忽略漏洞：

`snyk wizard`