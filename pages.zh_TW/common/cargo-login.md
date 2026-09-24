# cargo login

> 將來自註冊表的 API 權杖儲存到本地。
> 該權杖用於對套件註冊表進行身分驗證。您可以使用 `cargo logout` 來刪除它。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-login.html>。

- 將 API 權杖新增到本地憑證儲存中（位於 `$CARGO_HOME/credentials.toml`）：

`cargo login`

- 使用指定的註冊表（註冊表名稱可以在設定中定義，預設為 <https://crates.io>）：

`cargo login --registry {{名稱}}`
