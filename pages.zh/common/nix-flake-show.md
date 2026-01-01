# nix flake show

> 展示由 flake 提供的输出项。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-show.html>。

- 显示当前目录下 flake 的全部输出：

`nix flake show`

- 显示位于 GitHub 上的某个 flake 的全部输出，并以单行 JSON 格式打印：

`nix flake show {{github:owner/repo}} --json --no-pretty`

- 显示位于 GitHub 上的某个 flake 的全部 `legacyPackages` 输出，并以多行缩进的 JSON 格式打印：

`nix flake show {{github:owner/repo}} --json --pretty --legacy`

- 列出可用于 `nix flake init` 的所有 flake 模板：

`nix flake show templates`

