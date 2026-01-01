# nix build

> 构建 Nix 表达式（尽可能从缓存下载）。
> 另请参阅：`nix-build`，`nix flake`。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-build.html>。

- 从 nixpkgs 构建包，并将结果符号链接到 `./result`：

`nix build {{nixpkgs#包名}}`

- 构建当前目录中 Flake 的包，并显示构建日志：

`nix build {{[-L|--print-build-logs]}} {{.#包名}}`

- 构建某目录中 Flake 的默认包：

`nix build {{目录路径}}`

- 构建包但不创建 `result` 符号链接，而是将存储路径输出到标准输出：

`nix build --no-link --print-out-paths`
