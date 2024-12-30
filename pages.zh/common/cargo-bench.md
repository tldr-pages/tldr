# cargo bench

> 编译并执行基准测试。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-bench.html>。

- 执行一个包的所有基准测试：

`cargo bench`

- 当基准测试失败时不停止：

`cargo bench --no-fail-fast`

- 编译，但不运行基准测试：

`cargo bench --no-run`

- 基准测试指定的基准：

`cargo bench --bench {{benchmark}}`

- 使用给定的配置文件进行基准测试（默认：`bench`）：

`cargo bench --profile {{profile}}`

- 基准测试所有示例目标：

`cargo bench --examples`

- 基准测试所有二进制目标：

`cargo bench --bins`

- 基准测试包的库：

`cargo bench --lib`