# cargo owner

> 管理套件（crate）在註冊表上的所有者。
> 更多資訊：<https://doc.rust-lang.org/cargo/commands/cargo-owner.html>。

- 邀請指定的使用者或團隊作為所有者：

`cargo owner {{[-a|--add]}} {{使用者名稱|github:機構名稱:團隊名稱}} {{套件名稱}}`

- 將指定的使用者或團隊從所有者中刪除：

`cargo owner {{[-r|--remove]}} {{使用者名稱|github:機構名稱:團隊名稱}} {{套件名稱}}`

- 列出一個套件（crate）的所有者：

`cargo owner {{[-l|--list]}} {{套件名稱}}`

- 使用指定的註冊表（註冊表名稱可以在配置中定義，預設為 <https://crates.io>）：

`cargo owner --registry {{名稱}}`
