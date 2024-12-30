# tsort

> 执行拓扑排序。
> 一个常见的用途是显示有向无环图中节点的依赖顺序。
> 更多信息：<https://www.gnu.org/software/coreutils/tsort>。

- 对每行输入进行一致的拓扑排序，使用空格分隔：

`tsort {{path/to/file}}`

- 在字符串上执行一致的拓扑排序：

`echo -e "{{UI Backend\nBackend Database\nDocs UI}}" | tsort`