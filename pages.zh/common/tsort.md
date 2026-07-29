# tsort

> 执行拓扑排序。
> 常见用途是显示有向无环图中节点的依赖顺序。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tsort-invocation.html>。

- 执行拓扑排序，与每行输入中以空格分隔的部分排序一致：

`tsort {{路径/到/文件}}`

- 对字符串执行拓扑排序：

`echo -e "{{UI 后端\n后端 数据库\n文档 UI}}" | tsort`
