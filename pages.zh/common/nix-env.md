# nix-env

> 管理或查询 Nix 用户环境。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/nix-env.html>.

- 列出所有已安装的软件包：

`nix-env {{[-q|--query]}}`

- 查询已安装的软件包（支持 `正则表达式`）：

`nix-env {{[-q|--query]}} {{搜索模式}}`

- 从 Nixpkgs 注册表中查询可用的软件包：

`nix-env {{[-qa|--query --available]}} {{搜索模式}}`

- 从 Nixpkgs 注册表中安装软件包：

`nix-env {{[-iA|--install --attr]}} nixpkgs.{{软件包名称}}`

- 从自定义 URL 安装软件包：

`nix-env {{[-i|--install]}} {{软件包名称}} {{[-f|--file]}} {{example.com}}`

- 卸载软件包：

`nix-env {{[-e|--uninstall]}} {{软件包名称}}`

- 升级软件包：

`nix-env {{[-u|--upgrade]}} {{软件包名称}}`

- 获取特定操作（`--install`、`--upgrade` 等）的使用帮助：

`nix-env --help --{{选项名称}}`
