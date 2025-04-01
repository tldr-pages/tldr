# rustup override

> 修改目录的工具链覆盖设置。
> 有关工具链的更多信息，请参阅 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 列出目录的工具链覆盖设置：

`rustup override list`

- 为当前目录设置工具链覆盖（即告诉 `rustup` 当在该目录中时，从特定工具链运行 `cargo`、`rustc` 等）：

`rustup override set {{toolchain}}`

- 移除当前目录的工具链覆盖设置：

`rustup override unset`

- 移除所有不存在目录的工具链覆盖设置：

`rustup override unset --nonexistent`