# nix edit

> 在 `$EDITOR` 中打开 Nix 包的 Nix 表达式文件。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-edit.html>。

- 在 `$EDITOR` 中打开 nixpkgs 中指定包的 Nix 表达式源码：

`nix edit {{nixpkgs#软件包}}`

- 将包的源码直接打印输出至标准输出 (stdout)：

`EDITOR=cat nix edit {{nixpkgs#软件包}}`

