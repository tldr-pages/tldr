# unshadow

> John the Ripper 项目提供的工具，用于在系统使用影子密码时获取传统的 Unix 密码文件。
> 更多信息：<https://www.openwall.com/john/>.

- 合并当前系统的 `/etc/shadow` 和 `/etc/passwd` 文件：

`sudo unshadow /etc/passwd /etc/shadow`

- 合并任意的影子密码文件和密码文件：

`sudo unshadow {{path/to/passwd}} {{path/to/shadow}}`
