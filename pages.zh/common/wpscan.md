# wpscan

> WordPress 漏洞扫描工具。
> 更多信息：<https://github.com/wpscanteam/wpscan>.

- 更新漏洞数据库：

`wpscan --update`

- 扫描 WordPress 网站：

`wpscan --url {{url}}`

- 使用随机用户代理和被动检测方式扫描 WordPress 网站：

`wpscan --url {{url}} --stealthy`

- 扫描 WordPress 网站，检查易受攻击的插件，并指定 `wp-content` 目录的路径：

`wpscan --url {{url}} --enumerate {{vp}} --wp-content-dir {{远程路径/to/wp-content}}`

- 通过代理服务器扫描 WordPress 网站：

`wpscan --url {{url}} --proxy {{协议://ip:端口}} --proxy-auth {{用户名:密码}}`

- 在 WordPress 网站上执行用户标识枚举：

`wpscan --url {{url}} --enumerate {{u}}`

- 对 WordPress 网站执行密码猜测攻击：

`wpscan --url {{url}} --usernames {{用户名|用户名文件路径}} --passwords {{密码文件路径}} threads {{20}}`

- 扫描 WordPress 网站，从 WPVulnDB (<https://wpvulndb.com/>) 收集漏洞数据：

`wpscan --url {{url}} --api-token {{token}}`