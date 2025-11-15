# cargo login

> 将 API 令牌保存到本地的凭据存储中。
> 该令牌用于对包注册表进行身份验证。您可以使用 `cargo logout` 来删除它。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-login.html>.

- 将 API 令牌添加到本地凭据存储中 (位于 `$CARGO_HOME/credentials.toml`)：

`cargo login`

- 使用指定的注册表 (注册表名称可以在配置中定义，默认为 <https://crates.io>)：

`cargo login --registry {{名称}}`
