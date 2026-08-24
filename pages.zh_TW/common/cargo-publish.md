# cargo publish

> 將套件上傳到註冊表。
> 注意：在發布套件之前，您必須使用 `cargo login` 新增身份驗證權杖。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-publish.html>。

- 執行檢查，建立一個 `.crate` 檔案並將其上傳到註冊表：

`cargo publish`

- 執行檢查，建立一個 `.crate` 檔案，但不上傳它（相當於 `cargo package`）：

`cargo publish {{[-n|--dry-run]}}`

- 使用指定的註冊表（註冊表名稱可以在設定中定義，預設為 <https://crates.io>）：

`cargo publish --registry {{名稱}}`
