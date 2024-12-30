# wpscan

> WordPress 漏洞扫描器。
> 更多信息：<https://github.com/wpscanteam/wpscan>。

- 更新漏洞数据库：

`wpscan --update`

- 扫描一个 WordPress 网站：

`wpscan --url {{url}}`

- 扫描一个 WordPress 网站，使用随机用户代理和被动检测：

`wpscan --url {{url}} --stealthy`

- 扫描一个 WordPress 网站，检查易受攻击的插件并指定 `wp-content` 目录的路径：

`wpscan --url {{url}} --enumerate {{vp}} --wp-content-dir {{remote/path/to/wp-content}}`

- 通过代理扫描一个 WordPress 网站：

`wpscan --url {{url}} --proxy {{protocol://ip:port}} --proxy-auth {{username:password}}`

- 对一个 WordPress 网站执行用户标识符枚举：

`wpscan --url {{url}} --enumerate {{u}}`

- 对一个 WordPress 网站执行密码猜测攻击：

`wpscan --url {{url}} --usernames {{username|path/to/usernames.txt}} --passwords {{path/to/passwords.txt}} threads {{20}}`

- 扫描一个 WordPress 网站，从 WPVulnDB (<https://wpvulndb.com/>) 收集漏洞数据：

`wpscan --url {{url}} --api-token {{token}}`