# cargo yank

> 从索引中移除发布的包。应该只在意外发布了一个严重错误的包时使用。
> 注意：这不会删除任何数据。包在被撤回后仍然存在，只是阻止新项目使用它。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-yank.html>.

- 撤回指定版本的包：

`cargo yank {{包名}}@{{版本号}}`

- 撤销撤回 (即允许再次下载)：

`cargo yank --undo {{包名}}@{{版本号}}`

- 使用指定的注册表 (注册表名称可以在配置中定义 - 默认为 <https：//crates.io>)：

`cargo yank --registry {{名称}} {{包名}}@{{版本号}}`
