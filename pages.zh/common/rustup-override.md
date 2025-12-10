# rustup override

> 修改目录的工具链覆盖设置。
> 有关工具链的更多信息，请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>.

- 列出目录的工具链覆盖设置：

`rustup override list`

- 为当前目录设置覆盖工具链（即在该目录中运行 `cargo`、`rustc` 等命令时使用指定工具链）：

`rustup override set {{工具链}}`

- 移除当前目录的工具链覆盖设置：

`rustup override unset`

- 移除所有指向已不存在目录的工具链覆盖设置：

`rustup override unset --nonexistent`
