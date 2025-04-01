# nix edit

> 在 $EDITOR 中打开 Nix 包的 Nix 表达式。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-edit.html>。

- 在你的 `$EDITOR` 中打开来自 nixpkgs 的包的 Nix 表达式的源代码：

`nix edit {{nixpkgs#pkg}}`

- 将包的源代码输出到 `stdout`：

`EDITOR=cat nix edit {{nixpkgs#pkg}}`
