# Remove-NodeVersion

> Uninstall Node.js runtime versions for `ps-nvm`.
> This command is part of `ps-nvm` and can only be run under PowerShell.
> More information: <https://github.com/aaronpowell/ps-nvm>.

- Uninstall a given Node.js version:

`Remove-NodeVersion {{node_version}}`

- Uninstall multiple Node.js versions:

`Remove-NodeVersion {{node_version1 , node_version2 , ...}}`

- Uninstall all currently-installed versions of Node.js 20.x:

`Get-NodeVersions -Filter ">=20.0.0 <21.0.0" | Remove-NodeVersion`

- Uninstall all currently-installed versions of Node.js:

`Get-NodeVersions | Remove-NodeVersion`
