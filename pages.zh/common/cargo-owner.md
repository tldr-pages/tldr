# cargo owner

> 管理注册表中一个 crate 的所有者。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-owner.html>。

- 邀请指定用户或团队作为所有者：

`cargo owner --add {{username|github:org_name:team_name}} {{crate}}`

- 移除指定用户或团队作为所有者：

`cargo owner --remove {{username|github:org_name:team_name}} {{crate}}`

- 列出 crate 的所有者：

`cargo owner --list {{crate}}`

- 使用指定的注册表（注册表名称可以在配置中定义 - 默认是 <https://crates.io>）：

`cargo owner --registry {{name}}`