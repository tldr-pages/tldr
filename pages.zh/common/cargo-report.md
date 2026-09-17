# cargo report

> 显示各种类型的报告。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-report.html>。

- 显示一份属于未来将无法编译的包（crate）的报告：

`cargo report future-incompatibilities`

- 显示具有指定 Cargo 生成标识符的报告：

`cargo report future-incompatibilities --id {{标识符}}`

- 为指定的软件包显示报告：

`cargo report future-incompatibilities {{[-p|--package]}} {{软件包}}`
