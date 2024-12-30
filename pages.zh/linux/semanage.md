# semanage

> SELinux 持久策略管理工具。
> 一些子命令，如 `boolean`、`fcontext`、`port` 等，有自己的使用文档。
> 更多信息：<https://manned.org/semanage>。

- 设置或取消 SELinux 布尔值。布尔值允许管理员自定义策略规则如何影响受限进程类型（即域）：

`sudo semanage boolean {{-m|--modify}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`

- 添加用户定义的文件上下文标签规则。文件上下文定义了受限域允许访问的文件：

`sudo semanage fcontext {{-a|--add}} {{-t|--type}} {{samba_share_t}} '/mnt/share(/.*)?'`

- 添加用户定义的端口标签规则。端口标签定义了受限域允许监听的端口：

`sudo semanage port {{-a|--add}} {{-t|--type}} {{ssh_port_t}} {{-p|--proto}} {{tcp}} {{22000}}`

- 设置或取消受限域的宽松模式。每个域的宽松模式允许比 `setenforce` 更细粒度的控制：

`sudo semanage permissive {{-a|--add|-d|--delete}} {{httpd_t}}`

- 输出默认存储中的本地自定义：

`sudo semanage export {{-f|--output_file}} {{path/to/file}}`

- 将由 `semanage export` 生成的文件导入本地自定义（小心：可能会删除当前自定义！）：

`sudo semanage import {{-f|--input_file}} {{path/to/file}}`