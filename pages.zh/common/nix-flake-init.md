# nix flake init

> 基于模板在当前目录下创建一个flake。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake-init.html>。

- 在当前目录下使用默认模板创建新的flake：

`nix flake init`

- 使用指定的模板创建新的flake（关于模板信息，参见 `nix flake show`）：

`nix flake init {{[-t|--template]}} templates#{{your_template}}`