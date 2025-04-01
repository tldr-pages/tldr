# nix repl

> 启动一个用于评估 Nix 表达式的交互式环境。
> 有关 Nix 表达式语言的描述，请参见：<https://nixos.org/manual/nix/stable/language/index.html>。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-repl.html>。

- 启动一个用于评估 Nix 表达式的交互式环境：

`nix repl`

- 从一个 flake（例如 `nixpkgs`）加载所有包到作用域：

`:lf {{nixpkgs}}`

- 从表达式构建一个包：

`:b {{expression}}`

- 启动一个包含来自表达式的包的 shell：

`:u {{expression}}`

- 启动一个包含来自表达式的包的依赖项的 shell：

`:s {{expression}}`