# chcon

> 更改文件或文件夹的SELinux安全上下文。
> 另见：`secon`，`restorecon`，`semanage-fcontext`。
> 更多信息：<https://www.gnu.org/software/coreutils/chcon>。

- 查看文件的安全上下文：

`ls -lZ {{path/to/file}}`

- 使用参考文件更改目标文件的安全上下文：

`chcon --reference={{reference_file}} {{target_file}}`

- 更改文件的完整SELinux安全上下文：

`chcon {{user}}:{{role}}:{{type}}:{{range/level}} {{filename}}`

- 仅更改SELinux安全上下文中的用户部分：

`chcon -u {{user}} {{filename}}`

- 仅更改SELinux安全上下文中的角色部分：

`chcon -r {{role}} {{filename}}`

- 仅更改SELinux安全上下文中的类型部分：

`chcon -t {{type}} {{filename}}`

- 仅更改SELinux安全上下文中的范围/级别部分：

`chcon -l {{range/level}} {{filename}}`