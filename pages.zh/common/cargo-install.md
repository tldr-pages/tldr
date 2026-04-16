# cargo install

> 构建并安装一个 Rust 二进制文件。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-install.html>。

- 从 <https://crates.io> 安装一个软件包 (版本是可选的，默认为最新版本)：

`cargo install {{软件包}}@{{版本号}}`

- 从指定的 Git 仓库安装一个软件包：

`cargo install --git {{仓库 URL}}`

- 从 Git 仓库安装时，根据指定的 branch/tag/commit 构建：

`cargo install --git {{仓库 URL}} --{{branch|tag|rev}} {{branch_name|tag|commit_hash}}`

- 从本地目录安装一个软件包：

`cargo install --path {{路径/到/软件包}}`

- 列出所有已安装的软件包及其版本：

`cargo install --list`
