# cargo build

> 編譯本地套件及其所有相依項。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-build.html>。

- 在本地路徑中組建由 `Cargo.toml` 清單檔案定義的一個或多個套件：

`cargo {{[b|build]}}`

- 以 release 模式組建，並進行最佳化：

`cargo {{[b|build]}} {{[-r|--release]}}`

- 要求 `Cargo.lock` 檔案為最新版本：

`cargo {{[b|build]}} --locked`

- 組建工作區中的所有套件：

`cargo {{[b|build]}} --workspace`

- 組建特定的套件：

`cargo {{[b|build]}} {{[-p|--package]}} {{套件名}}`

- 僅組建指定的二進位檔案：

`cargo {{[b|build]}} --bin {{名稱}}`

- 僅組建指定的測試目標：

`cargo {{[b|build]}} --test {{測試名稱}}`
