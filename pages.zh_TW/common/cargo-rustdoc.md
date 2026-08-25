# cargo rustdoc

> 組建 Rust 套件的文件。
> 類似於 `cargo doc`，但您可以向 `rustdoc` 傳遞選項。查看 `rustdoc --help` 取得所有可用選項。
> 另請參閱：`rustdoc`。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>。

- 向 `rustdoc` 傳遞選項：

`cargo rustdoc -- {{rustdoc_options}}`

- 關於文件 lint 發出警告：

`cargo rustdoc -- {{[-W|--warn]}} rustdoc::{{lint_name}}`

- 忽略文件 lint：

`cargo rustdoc -- {{[-A|--allow]}} rustdoc::{{lint_name}}`

- 為套件的函式庫組建文件：

`cargo rustdoc --lib`

- 為指定的二進位檔案組建文件：

`cargo rustdoc --bin {{名稱}}`

- 為指定的範例組建文件：

`cargo rustdoc --example {{名稱}}`

- 為指定的整合測試組建文件：

`cargo rustdoc --test {{名稱}}`
