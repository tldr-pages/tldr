# npm profile

> Manage your npm profile and related settings.
> Note: This command is unaware of workspaces.
> More information: <https://docs.npmjs.com/cli/npm-profile>.

- View your npm profile details:

`npm profile get`

- View a specific property of your profile:

`npm profile get {{property}}`

- Set or update a profile property:

`npm profile set {{property}} {{value}}`

- Set your public email address:

`npm profile set email {{email}}`

- Set your public name:

`npm profile set name {{name}}`

- Enable two-factor authentication (2FA) (defaults to `auth-and-writes`):

`npm profile enable-2fa {{auth-only|auth-and-writes}}`

- Disable two-factor authentication (2FA):

`npm profile disable-2fa`
