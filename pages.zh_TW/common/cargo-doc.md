# cargo doc

> 組建 Rust 套件的文件。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-doc.html>。

- 為目前專案及所有相依項組建文件：

`cargo {{[d|doc]}}`

- 不為相依項組建文件：

`cargo {{[d|doc]}} --no-deps`

- 組建並在瀏覽器中開啟文件：

`cargo {{[d|doc]}} --open`

- 組建並檢視特定套件的文件：

`cargo {{[d|doc]}} --open {{[-p|--package]}} {{套件}}`
