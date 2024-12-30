# cargo tree

> 显示依赖关系图的树状可视化。
> 注意：在树中，标记为 `(*)` 的包的依赖关系已在图中的其他地方显示，因此不会重复。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-tree.html>。

- 显示当前项目的依赖树：

`cargo tree`

- 仅显示到指定深度的依赖关系（例如，当 `n` 为 1 时，仅显示直接依赖）：

`cargo tree --depth {{n}}`

- 不在树中显示给定包（及其依赖关系）：

`cargo tree --prune {{package_spec}}`

- 显示重复依赖关系的所有出现：

`cargo tree --no-dedupe`

- 仅显示正常/构建/开发依赖：

`cargo tree --edges {{normal|build|dev}}`