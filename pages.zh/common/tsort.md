# tsort

> 执行拓扑排序。
> 常用于显示有向无环图中节点的依赖顺序。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tsort-invocation.html>.

- 对输入文件中每行以空格分隔的部分排序，执行与部分排序一致的拓扑排序：

`tsort {{path/to/file}}`

- 对字符串执行拓扑排序：

`echo -e "{{UI Backend\nBackend Database\nDocs UI}}" | tsort`