# packwiz

> 创建、编辑和管理 Minecraft 模组包。
> 更多信息：<https://packwiz.infra.link/reference/commands/packwiz/>.

- 在当前目录中交互式创建一个新的模组包：

`packwiz init`

- 从 Modrinth 或 Curseforge 添加一个模组：

`packwiz {{modrinth|curseforge}} add {{url|slug|search_term}}`

- 列出模组包中的所有模组：

`packwiz list`

- 在手动编辑文件后更新 `index.toml`：

`packwiz refresh`

- 导出为 Modrinth (`.mrpack`) 或 Curseforge (Zip) 文件：

`packwiz {{modrinth|curseforge}} export`