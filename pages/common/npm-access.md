# npm access

> Set access level on published packages.
> More information: <https://docs.npmjs.com/cli/npm-access>.

- List packages for a user or scope:

`npm access list packages {{user|scope|scope:team}} {{package_name}}`

- List collaborators on a package:

`npm access list collaborators {{package_name}} {{username}}`

- Get status of a package:

`npm access get status {{package_name}}`

- Set package status (public or private):

`npm access set status {{public|private}} {{package_name}}`

- Grant access to a package:

`npm access grant {{read-only|read-write}} {{scope:team}} {{package_name}}`

- Revoke access to a package:

`npm access revoke {{scope:team}} {{package_name}}`

- Configure two-factor authentication requirement:

`npm access set mfa {{none|publish|automation}} {{package_name}}`
