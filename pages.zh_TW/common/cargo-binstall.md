# cargo binstall

> 從 CI 產物安裝 Rust 二進位檔案。
> 如果沒有可用的二進位檔案，則回退到 `cargo install`（從原始碼安裝）。
> 更多資訊：<https://github.com/cargo-bins/cargo-binstall>。

- 從 <https://crates.io> 安裝一個套件：

`cargo binstall {{套件}}`

- 安裝指定版本的套件（預設為最新版本）：

`cargo binstall {{套件}}@{{版本號}}`

- 安裝套件並停用確認提示：

`cargo binstall {{[-y|--no-confirm]}} {{套件}}`
