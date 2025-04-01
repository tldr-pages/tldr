# semanage

> SELinux 持久策略管理工具。
> 一些子命令如 `boolean`、`fcontext`、`port` 等有各自的使用文档。
> 更多信息：<https://manned.org/semanage>。

- 设置或取消设置 SELinux 布尔值。布尔值允许管理员自定义策略规则如何影响受限进程类型（即域）：

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`

- 添加用户定义的文件上下文标记规则。文件上下文定义了受限域允许访问的文件：

`sudo semanage fcontext {{[-a|--add]}} {{[-t|--type]}} {{samba_share_t}} '/mnt/share(/.*)?'`

- 添加用户定义的端口标记规则。端口标记定义了受限域允许监听的端口：

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{ssh_port_t}} {{[-p|--proto]}} {{tcp}} {{22000}}`

- 设置或取消设置受限域的宽容模式。每个域的宽容模式与 `setenforce` 相比提供了更细粒度的控制：

`sudo semanage permissive {{-a|--add|-d|--delete}} {{httpd_t}}`

- 导出默认存储中的本地自定义设置：

`sudo semanage export {{[-f|--output_file]}} {{path/to/file}}`

- 将由 `semanage export` 生成的文件导入本地自定义设置（小心：可能会删除当前的自定义设置！）：

`sudo semanage import {{[-f|--input_file]}} {{path/to/file}}`