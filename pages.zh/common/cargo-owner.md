# cargo owner

> 管理包（crate）在注册表上的所有者。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-owner.html>。

- 邀请指定的用户或团队作为所有者：

`cargo owner {{[-a|--add]}} {{用户名|github:机构名称:团队名称}} {{包名}}`

- 将指定的用户或团队从所有者中删除：

`cargo owner {{[-r|--remove]}} {{用户名|github:机构名称:团队名称}} {{包名}}`

- 列出一个包（crate）的所有者：

`cargo owner {{[-l|--list]}} {{包名}}`

- 使用指定的注册表（注册表名称可以在配置中定义，默认为 <https://crates.io>）：

`cargo owner --registry {{名称}}`
