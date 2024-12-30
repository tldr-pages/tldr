# debsecan

> Debian安全分析器，一个用于列出特定Debian安装中漏洞的工具。
> 更多信息：<https://gitlab.com/fweimer/debsecan>。

- 列出当前主机上脆弱的已安装软件包：

`debsecan`

- 列出特定版本的脆弱已安装软件包：

`debsecan --suite {{release_code_name}}`

- 仅列出已修复的漏洞：

`debsecan --suite {{release_code_name}} --only-fixed`

- 仅列出不稳定版本（“sid”）的已修复漏洞，并邮件发送给root：

`debsecan --suite {{sid}} --only-fixed --format {{report}} --mailto {{root}} --update-history`

- 升级脆弱的已安装软件包：

`sudo apt upgrade $(debsecan --only-fixed --format {{packages}})`