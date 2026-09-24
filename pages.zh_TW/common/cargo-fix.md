# cargo fix

> 自動修復 `rustc` 報告的 lint 警告。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-fix.html>。

- 即使已經有編譯器錯誤，也要修復程式碼：

`cargo fix --broken-code`

- 即使工作目錄有更改，也要修復程式碼：

`cargo fix --allow-dirty`

- 將一個套件遷移到下一個 Rust 版本：

`cargo fix --edition`

- 修復套件的函式庫：

`cargo fix --lib`

- 修復指定的整合測試：

`cargo fix --test {{名稱}}`

- 修復工作區中的所有成員：

`cargo fix --workspace`
