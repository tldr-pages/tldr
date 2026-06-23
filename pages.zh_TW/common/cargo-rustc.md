# cargo rustc

> 編譯一個 Rust 套件。類似於 `cargo build`，但您可以向編譯器傳遞額外的選項。
> 查看 `rustc --help` 獲取所有可用選項。
> 另請參閱：`rustc`。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>。

- 組建套件並向 `rustc` 傳遞選項：

`cargo rustc -- {{rustc_options}}`

- 在 release 模式下組建，啟用最佳化：

`cargo rustc {{[-r|--release]}}`

- 使用針對目前 CPU 的特定架構最佳化編譯：

`cargo rustc {{[-r|--release]}} -- {{[-C|--codegen]}} target-cpu=native`

- 使用速度最佳化編譯：

`cargo rustc -- {{[-C|--codegen]}} opt-level={{1|2|3}}`

- 使用體積（[s]ize）最佳化編譯（`z` 也會關閉迴圈向量化）：

`cargo rustc -- {{[-C|--codegen]}} opt-level={{s|z}}`

- 檢查您的套件是否使用了不安全的程式碼：

`cargo rustc --lib -- -D unsafe-code`

- 組建特定的套件：

`cargo rustc {{[-p|--package]}} {{套件}}`

- 僅組建指定的二進位檔案：

`cargo rustc --bin {{名稱}}`
