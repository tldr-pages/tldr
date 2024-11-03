# npm-org

> Manage orgs.
> More information: <https://docs.npmjs.com/cli/commands/npm-org>.

- Add a new user to an org:

`npm org set {{org_name}} {{username}}`

- Change a user's role in an org:

`npm org set {{org_name}} {{username}} {{developer|admin|owner}}`

- Remove a user from an org:

`npm org rm {{org_name}} {{username}}`

- List all users in an org:

`npm org ls {{org_name}}`

- List all users in an org, outputted in JSON format:

`npm org ls {{org_name}} --json`

- Display a user's role in an org:

`npm org ls {{org_name}} {{username}}`
