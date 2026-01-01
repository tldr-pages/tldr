# nix run

> 从 Nix 软件包配置中运行一个应用程序。
> 另请参阅：`nix flake`。
> 详细信息请见：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-run.html>。

- 运行当前目录下软件包配置中的默认应用程序：

`nix run`

- 运行名称与 nixpkgs 中软件包名称匹配的命令（如果需要该软件包中的其他命令，请参阅 `tldr nix shell`）：

`nix run nixpkgs#{{软件包}}`

- 使用提供的参数运行命令：

`nix run nixpkgs#{{vim}} -- {{文件路径}}`

- 从远程代码库运行：

`nix run {{远程仓库}}:{{所有者}}/{{代码库}}`

- 使用指定的标签、修订版本或分支从远程代码库运行：

`nix run {{远程仓库}}:{{所有者}}/{{代码库}}/{{引用}}`

- 从远程代码库指定子目录和程序运行：

`nix run "{{远程仓库}}:{{所有者}}/{{代码库}}?dir={{目录名}}#{{程序}}"`

- 运行 GitHub 拉取请求中的软件包配置：

`nix run github:{{所有者}}/{{代码库}}/pull/{{编号}}/head`