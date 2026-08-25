# cargo package

> 將一個本地套件打包成一個可分發的 tarball（`.crate` 檔案）。
> 類似於 `cargo publish --dry-run`，但具有更多選項。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-package.html>。

- 執行檢查並建立一個 `.crate` 檔案（相當於 `cargo publish --dry-run`）：

`cargo package`

- 顯示將包含在 tarball 中的檔案，而不實際建立它：

`cargo package {{[-l|--list]}}`
