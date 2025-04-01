# runcon

> 在不同的 SELinux 安全上下文中运行程序。
> 另请参见：`secon`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/runcon-invocation.html>。

- 打印当前执行上下文的安全上下文：

`runcon`

- 指定运行命令的域：

`runcon {{[-t|--type]}} {{domain}}_t {{command}}`

- 指定运行命令时的上下文角色：

`runcon {{[-r|--role]}} {{role}}_r {{command}}`

- 指定运行命令时的完整上下文：

`runcon {{user}}_u:{{role}}_r:{{domain}}_t {{command}}`
