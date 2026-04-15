# cargo

> 管理 Rust 專案及其模組相依項（crates）。
> 此命令也有關於其子命令的文件，例如：`build`.
> 更多資訊：<https://doc.rust-lang.org/stable/cargo/>。

- 搜尋套件（crate）：

`cargo search {{搜尋關鍵詞}}`

- 安裝二進位套件（crate）：

`cargo install {{套件名}}`

- 列出已安裝的二進位套件（crate）：

`cargo install --list`

- 在指定目錄（或預設情況下在目前工作目錄）中建立一個新的二進位或函式庫 Rust 專案：

`cargo init --{{bin|lib}} {{路徑/至/目錄}}`

- 向目前目錄的 `Cargo.toml` 新增一個相依項：

`cargo add {{相依項}}`

- 使用 release 模式在目前目錄中組建 Rust 專案：

`cargo {{[b|build]}} {{[-r|--release]}}`

- 使用最新的編譯器在目前目錄中組建 Rust 專案（需要 `rustup`）：

`cargo +nightly {{[b|build]}}`

- 使用特定數量的執行緒組建（預設為邏輯 CPU 的數量）：

`cargo {{[b|build]}} {{[-j|--jobs]}} {{執行緒數}}`
