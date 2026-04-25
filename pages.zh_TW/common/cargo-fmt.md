# cargo fmt

> 在 Rust 專案中對所有原始檔案執行 `rustfmt`。
> 更多資訊：<https://github.com/rust-lang/rustfmt>。

- 格式化所有原始檔案：

`cargo fmt`

- 檢查格式錯誤，不對檔案進行寫入操作：

`cargo fmt --check`

- 將參數傳遞給每個 rustfmt 呼叫：

`cargo fmt -- {{rustfmt參數}}`
