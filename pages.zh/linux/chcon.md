# chcon

> 更改文件或文件/目录的 SELinux 安全上下文。
> 参见：`secon`, `restorecon`, `semanage-fcontext`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>。

- 查看文件的安全上下文：

`ls {{[-lZ|-l --context]}} {{path/to/file}}`

- 使用参考文件更改目标文件的安全上下文：

`chcon --reference {{reference_file}} {{target_file}}`

- 更改文件的完整 SELinux 安全上下文：

`chcon {{user}}:{{role}}:{{type}}:{{range/level}} {{filename}}`

- 仅更改 SELinux 安全上下文的用户部分：

`chcon {{[-u|--user]}} {{user}} {{filename}}`

- 仅更改 SELinux 安全上下文的角色部分：

`chcon {{[-r|--role]}} {{role}} {{filename}}`

- 仅更改 SELinux 安全上下文的类型部分：

`chcon {{[-t|--type]}} {{type}} {{filename}}`

- 仅更改 SELinux 安全上下文的范围/级别部分：

`chcon {{[-l|--range]}} {{range/level}} {{filename}}`
