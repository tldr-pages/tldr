# npm team

> Manage teams in an organization on the `npm` registry.
> More information: <https://docs.npmjs.com/cli/npm-team>.

- Add a user to a team in an organization:

`npm team add {{organization:team}} {{username}}`

- Remove a user from a team:

`npm team rm {{organization:team}} {{username}}`

- Create a new team in an organization:

`npm team create {{organization:team}}`

- Delete a team from an organization:

`npm team destroy {{organization:team}}`

- List all teams in an organization:

`npm team ls {{organization}}`

- List all users in a specific team:

`npm team ls {{organization:team}}`
