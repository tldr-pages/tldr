# cargo bench

> 编译并执行基准测试。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- 执行包的所有基准测试：

`cargo bench`

- 在基准测试失败时不停止：

`cargo bench --no-fail-fast`

- 编译，但不运行基准测试：

`cargo bench --no-run`

- 对指定的基准进行基准测试：

`cargo bench --bench {{基准测试名称}}`

- 使用给定的配置文件进行基准测试 (默认为 `bench`)：

`cargo bench --profile {{配置文件}}`

- 对所有示例目标进行基准测试：

`cargo bench --examples`

- 对所有二进制目标进行基准测试：

`cargo bench --bins`

- 对包的库(lib)进行基准测试：

`cargo bench --lib`
