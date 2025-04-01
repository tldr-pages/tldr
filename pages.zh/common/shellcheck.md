# shellcheck

> 静态检查 shell 脚本中的错误、过时/不安全的功能使用情况和不良实践。
> 更多信息：<https://github.com/koalaman/shellcheck/wiki>.

- 检查一个 shell 脚本：

`shellcheck {{path/to/script.sh}}`

- 按指定的 [s]hell 方言检查一个 shell 脚本（覆盖脚本顶部的 shebang）：

`shellcheck --shell {{sh|bash|dash|ksh}} {{path/to/script.sh}}`

- 忽略一个或多个错误类型：

`shellcheck --exclude {{SC1009,SC1073,...}} {{path/to/script.sh}}`

- 同时检查任何被引用的 shell 脚本：

`shellcheck --check-sourced {{path/to/script.sh}}`

- 以指定的 [f]ormat 格式显示输出（默认为 `tty`）：

`shellcheck --format {{tty|checkstyle|diff|gcc|json|json1|quiet}} {{path/to/script.sh}}`

- 启用一个或多个 [o]ptional 检查：

`shellcheck --enable {{add-default-case,avoid-nullary-conditions,...}} {{path/to/script.sh}}`

- 列出所有默认情况下禁用的可选检查：

`shellcheck --list-optional`

- 调整考虑的 [S]everity 级别（默认为 `style`）：

`shellcheck --severity {{error|warning|info|style}} {{path/to/script.sh}}`