# cronic

> 用于包装 cron 作业的 Bash 脚本，以防止过多的电子邮件发送。
> 更多信息：<https://habilis.net/cronic/>.

- 调用一个命令，如果该命令返回非零退出代码，则显示其输出：

`cronic {{command}}`