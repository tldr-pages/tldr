# cs resolve

> 解析命令列出了其他依赖项的传递依赖项。
> 更多信息：<https://get-coursier.io/docs/cli-resolve>.

- 解析两个依赖项的传递依赖项列表：

`cs resolve {{group_id1}}:{{artifact_id1}}:{{artifact_version1}} {{group_id2}}:{{artifact_id2}}:{{artifact_version2}}`

- 通过依赖树解析包的传递依赖项列表：

`cs resolve --tree {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 以反向顺序解析依赖树（从一个依赖项到其依赖项）：

`cs resolve --reverse-tree {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- 打印依赖于特定库的所有库：

`cs resolve {{group_id}}:{{artifact_id}}:{{artifact_version}} --what-depends-on {{searched_group_id}}:{{searched_artifact_id}}`

- 打印依赖于特定库版本的所有库：

`cs resolve {{group_id}}:{{artifact_id}}:{{artifact_version}} --what-depends-on {{searched_group_id}}:{{searched_artifact_id}}{{searched_artifact_version}}`

- 打印一组包之间可能存在的冲突：

`cs resolve --conflicts {{group_id1:artifact_id1:artifact_version1 group_id2:artifact_id2:artifact_version2 ...}}`
