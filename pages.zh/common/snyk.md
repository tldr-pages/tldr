# snyk

> 查找代码中的漏洞并修复风险。
> 更多信息：<https://snyk.io>。

- 登录到您的 Snyk 账户：

`snyk auth`

- 测试您的代码是否存在已知漏洞：

`snyk test`

- 测试本地 Docker 镜像是否存在已知漏洞：

`snyk test --docker {{docker_image}}`

- 在 snyk.io 上记录依赖项的状态和任何漏洞：

`snyk monitor`

- 自动修补并忽略漏洞：

`snyk wizard`