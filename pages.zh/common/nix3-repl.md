# nix repl

> 开始一个交互环境以评估 Nix 表达式。
> 请参阅 <https://nixos.org/manual/nix/stable/language/index.html> 以了解 Nix 表达式语言的描述。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-repl.html>。

- 开始一个交互环境以评估 Nix 表达式：

`nix repl`

- 将所有来自 flake（例如 `nixpkgs`）的包加载到作用域中：

`:lf {{nixpkgs}}`

- 从表达式构建一个包：

`:b {{expression}}`

- 启动一个可用表达式中包的 shell：

`:u {{expression}}`

- 启动一个可用表达式中包依赖项的 shell：

`:s {{expression}}`