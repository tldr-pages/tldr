# cargo run

> 运行当前的 Cargo 包。
> 注意: 执行的二进制文件的工作目录将设置为当前工作目录。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- 运行默认的二进制目标：

`cargo {{[r|run]}}`

- 运行指定的二进制文件：

`cargo {{[r|run]}} --bin {{名称}}`

- 运行指定的示例：

`cargo {{[r|run]}} --example {{示例名}}`

- 激活一系列以空格或逗号分隔的功能：

`cargo {{[r|run]}} {{[-F|--features]}} "{{功能1 功能2 ...}}"`

- 禁用默认功能：

`cargo {{[r|run]}} --no-default-features`

- 激活所有可用的功能：

`cargo {{[r|run]}} --all-features`

- 使用指定的配置文件运行：

`cargo {{[r|run]}} --profile {{配置文件名称}}`
