# pio team

> Manage PlatformIO teams.
> More information: <https://docs.platformio.org/en/latest/core/userguide/team/index.html>.

- Create a new team with a description:

`pio team create --description {{description}} {{orgname}}:{{teamname}}`

- Delete a team:

`pio team destroy {{orgname}}:{{teamname}}`

- Add a new member to a team:

`pio team add {{orgname}}:{{teamname}} {{username}}`

- Remove a member from a team:

`pio team remove {{orgname}}:{{teamname}} {{username}}`

- List all teams and their members of an organisation:

`pio team list {{orgname}}`

- Rename a team and update its description:

`pio team update --name {{new_teamname}} --description {{new_description}} {{orgname}}:{{teamname}}`
