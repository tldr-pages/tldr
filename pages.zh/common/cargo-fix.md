# cargo fix

> 自动修复 `rustc` 报告的 lint 警告。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-fix.html>.

- 即使已经有编译器错误，也要修复代码：

`cargo fix --broken-code`

- 即使工作目录有更改，也要修复代码：

`cargo fix --allow-dirty`

- 将一个包迁移到下一个 Rust 版本：

`cargo fix --edition`

- 修复包的库：

`cargo fix --lib`

- 修复指定的集成测试：

`cargo fix --test {{名称}}`

- 修复工作区中的所有成员：

`cargo fix --workspace`
