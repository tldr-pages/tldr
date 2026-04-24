# cargo clean

> 刪除 `target` 目錄中產生的組建產物。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-clean.html>。

- 刪除整個 `target` 目錄：

`cargo clean`

- 刪除文件組建產物（`target/doc` 目錄）：

`cargo clean --doc`

- 刪除 release 模式的組建產物（`target/release` 目錄）：

`cargo clean {{[-r|--release]}}`

- 刪除指定設定檔的目錄中的組建產物（在此例中為 `target/debug`）：

`cargo clean --profile {{dev}}`
