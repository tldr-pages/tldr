# nix build

> 构建一个 Nix 表达式（尽可能从缓存中下载）。
> 另见：`nix-build` 了解有关传统 Nix 构建的更多信息，`nix3 flake` 了解有关 flakes 的信息。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-build.html>。

- 从 nixpkgs 构建一个包，并将结果符号链接到 `./result`：

`nix build {{nixpkgs#pkg}}`

- 从当前目录的 flake 构建一个包，并在过程中显示构建日志：

`nix build -L {{.#pkg}}`

- 从某个目录的 flake 构建默认包：

`nix build {{./path/to/directory}}`

- 构建一个包而不创建 `result` 符号链接，而是将存储路径打印到 `stdout`：

`nix build --no-link --print-out-paths`