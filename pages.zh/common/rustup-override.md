# rustup 覆盖

> 修改目录工具链覆盖。
> 详细信息请参见 `rustup help toolchain`。
> 更多信息：<https://rust-lang.github.io/rustup>。

- 列出目录工具链覆盖：

`rustup override list`

- 为当前目录设置覆盖工具链（即告诉 `rustup` 在该目录中从特定工具链运行 `cargo`、`rustc` 等）：

`rustup override set {{toolchain}}`

- 移除当前目录的工具链覆盖：

`rustup override unset`

- 移除所有不存在的目录的工具链覆盖：

`rustup override unset --nonexistent`