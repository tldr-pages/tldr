# pio access

> 设置注册表中已发布资源（包）的访问级别。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/access/>.

- 授予用户对资源的访问权限：

`pio access grant {{guest|maintainer|admin}} {{username}} {{resource_urn}}`

- 撤销用户对资源的访问权限：

`pio access revoke {{username}} {{resource_urn}}`

- 显示用户或团队拥有访问权限的所有资源及其访问级别：

`pio access list {{username}}`

- 限制资源的访问权限，仅特定用户或团队成员可访问：

`pio access private {{resource_urn}}`

- 允许所有用户访问资源：

`pio access public {{resource_urn}}`
