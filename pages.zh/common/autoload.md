# autoload

> 在 Zsh 中标记函数以进行延迟加载。
> 函数在首次调用之前不会加载到内存中，从而提高 shell 启动速度。
> 更多信息：<https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>。

- 按名称自动加载函数：

`autoload {{函数名称}}`

- 自动加载函数并立即解析其定义：

`autoload +X {{函数名称}}`

- 使用 Zsh 风格的自动加载（推荐）：

`autoload -Uz {{函数名称}}`

- 通过将目录添加到 `fpath` 使目录中的函数可用：

`fpath=({{路径/到/functions_dir}} $fpath) && autoload -Uz {{函数名称}}`

- 自动加载 Zsh 补全系统：

`autoload -Uz compinit && compinit`

- 自动加载并使用 `add-zsh-hook` 实用程序：

`autoload -Uz add-zsh-hook`
