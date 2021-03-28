# pio team

> Manage PlatformIO teams.
> More information: <https://docs.platformio.org/en/latest/core/userguide/team/>.

- Create a new team with the specified description:

`pio team create --description {{description}} {{orgname}}:{{team_name}}`

- Delete a team:

`pio team destroy {{organization_name}}:{{team_name}}`

- Add a new user to a team:

`pio team add {{organization_name}}:{{team_name}} {{username}}`

- Remove a user from a team:

`pio team remove {{organization_name}}:{{team_name}} {{username}}`

- List all teams and their members, the user is part of:

`pio team list`

- List all teams and their members of an organisation:

`pio team list {{organization_name}}`

- Rename a team:

`pio team update --name {{new_teamname}} {{organization_name}}:{{team_name}}`

- Change the description of a team:

`pio team update --description {{new_description}} {{organization_name}}:{{team_name}}`
