# nix flake info

> 显示 flake 的元数据信息。
> 更多信息： <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-info>.

- 显示当前目录下的 flake 元数据信息：

`nix flake info`

- 以单行 JSON 格式显示来自 GitHub 的 flake 元数据信息：

`nix flake info {{github:owner/repo}} --json --no-pretty`

- 以多行缩进 JSON 格式显示来自 GitHub 的 flake 元数据信息：

`nix flake info {{github:owner/repo}} --json --pretty`
