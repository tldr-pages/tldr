# cargo add

> 向 Rust 專案的 `Cargo.toml` 清單新增相依項。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-add.html>。

- 將最新版本的相依項新增到目前專案：

`cargo add {{相依項}}`

- 新增特定版本的相依項：

`cargo add {{相依項}}@{{版本號}}`

- 新增相依項並啟用一或多個特定功能：

`cargo add {{相依項}} {{[-F|--features]}} {{功能1,功能2,...}}`

- 新增一個選用的相依項，然後將其作為套件（crate）的一個功能暴露出來：

`cargo add {{相依項}} --optional`

- 將本地套件（crate）新增為相依項：

`cargo add --path {{路徑/至/目錄}}`

- 新增一個開發或組建相依項：

`cargo add {{相依項}} --{{dev|build}}`

- 新增一個停用所有預設功能的相依項：

`cargo add {{相依項}} --no-default-features`
