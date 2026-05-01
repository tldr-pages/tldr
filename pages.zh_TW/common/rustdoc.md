# rustdoc

> 為 Rust 套件（crate）產生文件。
> 更多資訊：<https://doc.rust-lang.org/stable/rustdoc/>。

- 從套件（crate）的根檔案產生文件：

`rustdoc {{src/lib.rs}}`

- 為專案傳遞一個名稱：

`rustdoc {{src/lib.rs}} --crate-name {{名稱}}`

- 從 Markdown 檔案產生文件：

`rustdoc {{路徑/到/檔案.md}}`

- 指定輸出目錄：

`rustdoc {{src/lib.rs}} {{[-o|--out-dir]}} {{路徑/到/輸出目錄}}`

- 顯示說明：

`rustdoc {{[-h|--help]}}`
