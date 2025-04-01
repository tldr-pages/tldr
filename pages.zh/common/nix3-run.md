# nix run

> 从 Nix flake 中运行一个应用程序。
> 参见：`nix3 flake` 了解关于 flakes 的信息。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-run.html>。

- 运行当前目录中 flake 的默认应用程序：

`nix run`

- 从 nixpkgs 中运行与包名匹配的命令（如果你想运行该包中的其他命令，请参见 `tldr nix3 shell`）：

`nix run nixpkgs#{{pkg}}`

- 运行带有提供参数的命令：

`nix run nixpkgs#{{vim}} -- {{path/to/file}}`

- 从远程仓库运行命令：

`nix run {{remote_name}}:{{owner}}/{{repo}}`

- 从远程仓库使用特定标签、修订版或分支运行命令：

`nix run {{remote_name}}:{{owner}}/{{repo}}/{{reference}}`

- 从远程仓库指定子目录和程序：

`nix run "{{remote_name}}:{{owner}}/{{repo}}?dir={{dir_name}}#{{app}}"`

- 运行 GitHub 拉取请求中的 flake：

`nix run github:{{owner}}/{{repo}}/pull/{{number}}/head`
