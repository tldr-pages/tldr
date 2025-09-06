# cargo build

> 编译本地包及其所有依赖项。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- 在本地路径中构建由 `Cargo.toml` 清单文件定义的一个或多个包：

`cargo {{[b|build]}}`

- 以 release 模式构建，并进行优化：

`cargo {{[b|build]}} {{[-r|--release]}}`

- 要求 `Cargo.lock` 文件为最新版本：

`cargo {{[b|build]}} --locked`

- 构建工作区中的所有包：

`cargo {{[b|build]}} --workspace`

- 构建特定的包：

`cargo {{[b|build]}} {{[-p|--package]}} {{包名}}`

- 仅构建指定的二进制文件：

`cargo {{[b|build]}} --bin {{名称}}`

- 仅构建指定的测试目标：

`cargo {{[b|build]}} --test {{测试名称}}`
