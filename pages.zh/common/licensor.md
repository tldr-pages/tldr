# licensor

> 将许可证写入 `stdout`。
> 更多信息：<https://github.com/raftario/licensor>.

- 将 MIT 许可证写入名为 `LICENSE` 的文件：

`licensor {{MIT}} > {{LICENSE}}`

- 将 MIT 许可证及其占位符版权声明写入名为 `LICENSE` 的文件：

`licensor {{[-p|--keep-placeholder]}} {{MIT}} > {{LICENSE}}`

- 指定版权持有者为 Bobby Tables：

`licensor {{MIT}} "{{Bobby Tables}}" > {{LICENSE}}`

- 使用 WITH 表达式指定许可证例外：

`licensor "{{Apache-2.0 WITH LLVM-exception}}" > {{LICENSE}}`

- 列出所有可用的许可证：

`licensor {{[-l|--licenses]}}`

- 列出所有可用的例外：

`licensor {{[-e|--exceptions]}}`