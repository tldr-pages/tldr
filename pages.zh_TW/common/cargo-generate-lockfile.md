# cargo generate-lockfile

> 為目前套件產生 `Cargo.lock` 檔案。類似於 `cargo update`，但選項更少。
> 如果鎖定檔案已經存在，它將使用每個套件的最新版本重新組建。
> 更多資訊：<https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>。

- 使用每個套件的最新版本產生 `Cargo.lock` 檔案：

`cargo generate-lockfile`
