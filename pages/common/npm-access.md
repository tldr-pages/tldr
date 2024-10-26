# npm access

> Set access level on published packages.
> More information: <https://docs.npmjs.com/cli/npm-access>.

- List packages for a user or scope:

`npm access list packages [<user>|<scope>|<scope:team>] [<package>]`

- List collaborators on a package:

`npm access list collaborators [<package> [<user>]]`

- Get status of a package:

`npm access get status [<package>]`

- Set package status (public or private):

`npm access set status=public|private [<package>]`

- Grant access to a package:

`npm access grant <read-only|read-write> <scope:team> [<package>]`

- Revoke access to a package:

`npm access revoke <scope:team> [<package>]`

- Configure two-factor authentication requirement:

`npm access set mfa=none|publish|automation [<package>]`

If you need any additional details or changes, feel free to ask!
