# lnav

> 高级日志文件查看器，分析日志几乎不需要设置。
> 更多信息：<https://docs.lnav.org/en/latest/cli.html>。

- 查看程序的日志，指定日志文件、目录或URL：

`lnav {{path/to/log_or_directory|url}}`

- 查看特定远程主机的日志（需要无密码SSH登录）：

`lnav {{ssh}} {{user}}@{{host1.example.com}}:{{/var/log/syslog.log}}`

- 验证日志文件的格式与配置是否一致，并报告任何错误：

`lnav -C {{path/to/log_directory}}`