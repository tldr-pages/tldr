# nix run

> 从 Nix flake 运行一个应用程序。
> 另见：有关 flakes 的信息，请参见 `nix3 flake`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-run.html>。

- 在当前目录中运行 flake 的默认应用程序：

`nix run`

- 运行与 nixpkgs 中的包名匹配的命令（如果您想要该包中的不同命令，请参见 `tldr nix3 shell`）：

`nix run nixpkgs#{{pkg}}`

- 运行带有提供参数的命令：

`nix run nixpkgs#{{vim}} -- {{path/to/file}}`

- 从远程仓库运行：

`nix run {{remote_name}}:{{owner}}/{{repo}}`

- 使用特定标签、修订版或分支从远程仓库运行：

`nix run {{remote_name}}:{{owner}}/{{repo}}/{{reference}}`

- 从远程仓库指定子目录和程序运行：

`nix run "{{remote_name}}:{{owner}}/{{repo}}?dir={{dir_name}}#{{app}}"`

- 运行 GitHub 拉取请求的 flake：

`nix run github:{{owner}}/{{repo}}/pull/{{number}}/head`