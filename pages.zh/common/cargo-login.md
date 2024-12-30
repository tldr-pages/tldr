# cargo 登录

> 将 API 令牌从注册表保存到本地。
> 该令牌用于对包注册表进行身份验证。您可以使用 `cargo 登出` 将其删除。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-login.html>。

- 将 API 令牌添加到本地凭证存储（位于 `$CARGO_HOME/credentials.toml`）：

`cargo 登录`

- 使用指定的注册表（注册表名称可以在配置中定义 - 默认是 <https://crates.io>）：

`cargo 登录 --registry {{name}}`