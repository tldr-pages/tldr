# rustup set

> 修改 `rustup` 设置。
> 更多信息： <https://rust-lang.github.io/rustup>.

- 设置默认主机三元组：

`rustup set default-host {{host_triple}}`

- 设置默认配置文件（`minimal` 仅包含 `rustc`，`rust-std` 和 `cargo`，而 `default` 则添加 `rust-docs`，`rustfmt` 和 `clippy`）：

`rustup set profile {{minimal|default}}`

- 设置 `rustup` 是否在运行 `rustup update` 时自动更新自身：

`rustup set auto-self-update {{enable|disable|check-only}}`