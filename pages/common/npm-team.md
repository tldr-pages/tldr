# npm team

> Manage teams in an organization on the `npm` registry.
> More information: <https://docs.npmjs.com/cli/commands/npm-team>.

- Add a user to a team in an organization:

`npm team add {{scope:team}} {{username}}`

- Remove a user from a team:

`npm team rm {{scope:team}} {{username}}`

- Create a new team in an organization:

`npm team create {{scope:team}}`

- Delete a team from an organization:

`npm team destroy {{scope:team}}`

- List all teams in an organization:

`npm team ls {{scope}}`

- List all users in a specific team:

`npm team ls {{scope:team}}`
