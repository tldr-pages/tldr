# firejail

> 使用内置的Linux能力安全地将进程沙箱化到容器中。
> 更多信息：<https://manned.org/firejail>。

- 将firejail与您的桌面环境集成：

`sudo firecfg`

- 打开受限的Mozilla Firefox：

`firejail {{firefox}}`

- 在已知接口和地址上启动受限的Apache服务器：

`firejail --net={{eth0}} --ip={{192.168.1.244}} {{/etc/init.d/apache2}} {{start}}`

- 列出正在运行的沙箱：

`firejail --list`

- 列出正在运行的沙箱的网络活动：

`firejail --netstats`

- 关闭正在运行的沙箱：

`firejail --shutdown={{7777}}`

- 运行受限的Firefox会话以浏览互联网：

`firejail --seccomp --private --private-dev --private-tmp --protocol=inet firefox --new-instance --no-remote --safe-mode --private-window`

- 使用自定义hosts文件（覆盖`/etc/hosts`文件）：

`firejail --hosts-file={{~/myhosts}} {{curl http://mysite.arpa}}`