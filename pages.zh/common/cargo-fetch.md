# cargo fetch

> 从网络获取包的依赖项。
> 更多信息请访问：<https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>。

- 获取 `Cargo.lock` 中指定的依赖项（适用于所有目标）：

`cargo fetch`

- 获取指定目标的依赖项：

`cargo fetch --target {{target_triple}}`