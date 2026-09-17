# cargo remove

> 從 Rust 專案的 `Cargo.toml` 清單中移除相依項。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-remove.html>。

- 從目前專案中移除一個相依項：

`cargo remove {{相依項}}`

- 移除開發或組建相依項：

`cargo remove --{{dev|build}} {{相依項}}`

- 移除給定目標平台的相依項：

`cargo remove --target {{目标}} {{相依項}}`
