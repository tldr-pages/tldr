# cargo yank

> 从索引中移除已推送的 crate。只有在意外发布了严重损坏的 crate 时才应使用此功能。
> 注意：这不会删除任何数据。yank 之后，crate 仍然存在 - 这只是阻止新项目使用它。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-yank.html>。

- yank 指定版本的 crate：

`cargo yank {{crate}}@{{version}}`

- 撤销 yank（即允许再次下载）：

`cargo yank --undo {{crate}}@{{version}}`

- 使用指定的注册表（注册表名称可以在配置中定义 - 默认是 <https://crates.io>）：

`cargo yank --registry {{name}} {{crate}}@{{version}}`