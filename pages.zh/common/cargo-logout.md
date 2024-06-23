# cargo logout

> 从本地注册表中删除 API 令牌。
> 该令牌用于对包注册表进行身份验证。您可以使用 `cargo login` 将其添加回来。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- 从本地凭据存储中 (位于 `$CARGO_HOME/credentials.toml`) 移除 API 令牌：

`cargo logout`

- 使用指定的注册表 (注册表名称可以在配置中定义，默认为 <https://crates.io>)：

`cargo logout --registry {{名称}}`
