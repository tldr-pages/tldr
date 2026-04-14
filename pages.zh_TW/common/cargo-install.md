# cargo install

> 構建並安裝一個 Rust 二進制文件。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-install.html>。

- 從 <https://crates.io> 安裝一個包（版本是可選的，默認為最新版本）：

`cargo install {{包名}}@{{版本號}}`

- 從指定的 Git 倉庫安裝一個包：

`cargo install --git {{倉庫 URL}}`

- 從 Git 倉庫安裝時，根據指定的 branch/tag/commit 構建：

`cargo install --git {{倉庫 URL}} --{{branch|tag|rev}} {{branch_name|tag|commit_hash}}`

- 從本地目錄安裝一個包：

`cargo install --path {{路徑/至/目錄}}`

- 列出所有已安裝的包及其版本：

`cargo install --list`
