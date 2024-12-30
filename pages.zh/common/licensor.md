# 许可证

> 将许可证写入`stdout`。
> 更多信息：<https://github.com/raftario/licensor>。

- 将MIT许可证写入名为`LICENSE`的文件：

`licensor {{MIT}} > {{LICENSE}}`

- 将带有占位符版权声明的MIT许可证写入名为`LICENSE`的文件：

`licensor -p {{MIT}} > {{LICENSE}}`

- 指定版权持有人为Bobby Tables：

`licensor {{MIT}} "{{Bobby Tables}}" > {{LICENSE}}`

- 使用WITH表达式指定许可证例外：

`licensor "{{Apache-2.0 WITH LLVM-exception}}" > {{LICENSE}}`

- 列出所有可用的许可证：

`licensor --licenses`

- 列出所有可用的例外：

`licensor --exceptions`