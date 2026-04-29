# cargo locate-project

> 列印專案的 `Cargo.toml` 清單檔案的完整路徑。
> 如果專案是工作區的一部分，則顯示專案的清單檔案，而不是工作區的清單檔案。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>。

- 顯示包含完整路徑到 `Cargo.toml` 清單檔案的 JSON 物件：

`cargo locate-project`

- 以指定格式顯示專案路徑：

`cargo locate-project --message-format {{plain|json}}`

- 顯示位於工作區根目錄而不是目前工作區成員的 `Cargo.toml` 清單檔案：

`cargo locate-project --workspace`

- 顯示特定目錄中的 `Cargo.toml` 清單檔案：

`cargo locate-project --manifest-path {{path/to/Cargo.toml}}`
