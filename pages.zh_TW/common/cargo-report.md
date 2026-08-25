# cargo report

> 顯示各種類型的報告。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-report.html>。

- 顯示一份屬於未來將無法編譯的包（crate）的報告：

`cargo report future-incompatibilities`

- 顯示具有指定 Cargo 生成識別碼的報告：

`cargo report future-incompatibilities --id {{識別碼}}`

- 為指定的套件顯示報告：

`cargo report future-incompatibilities {{[-p|--package]}} {{套件}}`
