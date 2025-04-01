# debsecan

> Debian 安全分析器，用于列出特定 Debian 安装中的漏洞。
> 更多信息：<https://gitlab.com/fweimer/debsecan>。

- 列出当前主机上存在漏洞的已安装包：

`debsecan`

- 列出特定版本中存在漏洞的已安装包：

`debsecan --suite {{release_code_name}}`

- 仅列出已修复的漏洞：

`debsecan --suite {{release_code_name}} --only-fixed`

- 仅列出不稳定版本（"sid"）中已修复的漏洞，并将报告邮件发送给 root 用户：

`debsecan --suite {{sid}} --only-fixed --format {{report}} --mailto {{root}} --update-history`

- 升级存在漏洞的已安装包：

`sudo apt upgrade $(debsecan --only-fixed --format {{packages}})`