# rustfmt

> 格式化 Rust 源代码。
> 更多信息：<https://github.com/rust-lang/rustfmt>。

- 格式化文件，就地覆盖原始文件：

`rustfmt {{路径/到/源文件.rs}}`

- 检查文件的格式并在控制台显示所有变更：

`rustfmt --check {{路径/到/源文件.rs}}`

- 在格式化前备份所有修改的文件（原始文件会以 `.bk` 扩展名重命名）：

`rustfmt --backup {{路径/到/源文件.rs}}`

- 使用特定的 Rust 风格版次（格式化规则）以详细模式格式化代码：

`rustfmt --style-edition {{2015|2018|2021|2024}} {{[-v|--verbose]}} {{路径/到/源文件1.rs 路径/到/源文件2.rs ...}}`

- 使用特定的 Rust 版次（语言特性和解析）格式化代码：

`rustfmt --edition {{2015|2018|2021|2024}} {{路径/到/源文件1.rs 路径/到/源文件2.rs ...}}`
