# cargo metadata

> 以 JSON 格式输出当前包的工作空间成员和已解析的依赖关系。
> 注意：输出格式可能在未来的 Cargo 版本中发生变化。
> 更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-metadata.html>.

- 打印当前包的工作空间成员和已解析的依赖关系：

`cargo metadata`

- 仅打印工作空间成员，不获取依赖项：

`cargo metadata --no-deps`

- 根据指定版本打印特定格式的元数据：

`cargo metadata --format-version {{版本号}}`

- 打印带有 `resolve` 字段的元数据，仅包括给定目标三元组的依赖关系 (注意：`packages` 数组仍将包括所有目标的依赖关系)：

`cargo metadata --filter-platform {{目标三元组}}`
