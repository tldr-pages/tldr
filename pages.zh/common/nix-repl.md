# nix repl

> 启动一个用于计算 Nix 表达式的交互式环境。
> 有关 Nix 表达式语言的介绍，请参阅 <https://nixos.org/manual/nix/stable/language/index.html>。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-repl.html>.

- 启动一个用于计算 Nix 表达式的交互式环境：

`nix repl`

- 将所有包从某个 flake（例如 `nixpkgs`）加载到作用域中：

`:lf {{nixpkgs}}`

- 从表达式构建一个软件包：

`:b {{expression}}`

- 启动一个包含表达式所提供软件包的 shell 环境：

`:u {{expression}}`

- 启动一个包含表达式所提供软件包依赖项的 shell 环境：

`:s {{expression}}`
