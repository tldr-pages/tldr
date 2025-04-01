# pio team

> 管理 PlatformIO 团队。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/team/>.

- 创建一个具有指定描述的新团队：

`pio team create --description {{description}} {{organization_name}}:{{team_name}}`

- 删除一个团队：

`pio team destroy {{organization_name}}:{{team_name}}`

- 将新用户添加到团队中：

`pio team add {{organization_name}}:{{team_name}} {{username}}`

- 从团队中移除用户：

`pio team remove {{organization_name}}:{{team_name}} {{username}}`

- 列出用户所属的所有团队及其成员：

`pio team list`

- 列出组织中的所有团队：

`pio team list {{organization_name}}`

- 重命名团队：

`pio team update --name {{new_team_name}} {{organization_name}}:{{team_name}}`

- 更改团队的描述：

`pio team update --description {{new_description}} {{organization_name}}:{{team_name}}`
