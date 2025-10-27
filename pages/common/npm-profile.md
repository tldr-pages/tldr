# npm profile

> Manage your npm profile and related settings.
> Note: This command is unaware of workspaces.
> More information: <https://docs.npmjs.com/cli/npm-profile>.

- View your npm profile details:

`npm profile get`

- Set or update a profile property:

`npm profile set {{property}} {{value}}`

- View a specific property of your profile:

`npm profile get {{property}}`

- Enable two-factor authentication (2FA):

`npm profile enable-2fa {{auth-only|auth-and-writes}}`

- Disable two-factor authentication (2FA):

`npm profile disable-2fa`

- Set your public email address:

`npm profile set email {{email}}`

- Set your public name:

`npm profile set name {{name}}`
