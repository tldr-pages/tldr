# unshadow

> 由 John the Ripper 项目提供的工具，用于获取传统的 Unix 密码文件，如果系统使用阴影密码的话。
> 更多信息：<https://www.openwall.com/john/>.

- 合并当前系统的 `/etc/shadow` 和 `/etc/passwd`：

`sudo unshadow /etc/passwd /etc/shadow`

- 合并两个任意的阴影和密码文件：

`sudo unshadow {{path/to/passwd}} {{path/to/shadow}}`