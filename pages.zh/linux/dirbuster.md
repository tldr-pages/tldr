# dirbuster

> 对服务器上的目录和文件名进行暴力破解。
> 更多信息：<https://www.kali.org/tools/dirbuster/>.

- 以 GUI 模式启动：

`dirbuster -u {{http://example.com}}`

- 以无头（无 GUI）模式启动：

`dirbuster -H -u {{http://example.com}}`

- 设置文件扩展名列表：

`dirbuster -e {{txt,html}}`

- 启用详细输出：

`dirbuster -v`

- 设置报告保存位置：

`dirbuster -r {{path/to/report.txt}}`
