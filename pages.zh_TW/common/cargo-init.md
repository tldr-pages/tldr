# cargo init

> 創建一個新的 Cargo 套件。
> 相當於 `cargo new`，但是指定目錄是可選的。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-init.html>。

- 在目前目錄中初始化一個帶有二進位目標的 Rust 專案：

`cargo init`

- 在指定目錄中初始化一個帶有二進位目標的 Rust 專案：

`cargo init {{路徑/至/目錄}}`

- 在目前目錄中初始化一個帶有函式庫目標的 Rust 專案：

`cargo init --lib`

- 在專案目錄中初始化版本控制系統倉庫（預設為 `git`）：

`cargo init --vcs {{git|hg|pijul|fossil|none}}`

- 設定套件名稱（預設為目錄名稱）：

`cargo init --name {{名稱}}`
