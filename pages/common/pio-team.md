# pio team

> Manage PlatformIO teams.
> More information: <https://docs.platformio.org/en/latest/core/userguide/team/>.

- Create a new team with the specified description:

`pio team create --description {{description}} {{orgname}}:{{teamname}}`

- Delete a team:

`pio team destroy {{orgname}}:{{teamname}}`

- Add a new user to a team:

`pio team add {{orgname}}:{{teamname}} {{username}}`

- Remove a user from a team:

`pio team remove {{orgname}}:{{teamname}} {{username}}`

- List all teams and their members, the user is part of:

`pio team list`

- List all teams and their members of an organisation:

`pio team list {{orgname}}`

- Rename a team:

`pio team update --name {{new_teamname}} {{orgname}}:{{teamname}}`

- Change the description of a team:

`pio team update --description {{new_description}} {{orgname}}:{{teamname}}`
