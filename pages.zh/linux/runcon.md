# runcon

> 在不同的SELinux安全上下文中运行程序。
> 另见：`secon`。
> 更多信息：<https://www.gnu.org/software/coreutils/runcon>。

- 打印当前执行上下文的安全上下文：

`runcon`

- 指定要在其中运行命令的域：

`runcon -t {{domain}}_t {{command}}`

- 指定要以其运行命令的上下文角色：

`runcon -r {{role}}_r {{command}}`

- 指定要以其运行命令的完整上下文：

`runcon {{user}}_u:{{role}}_r:{{domain}}_t {{command}}`