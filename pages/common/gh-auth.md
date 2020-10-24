# gh-auth

> Authenticate with GitHub in GitHub cli.
> More information: <https://cli.github.com/manual/gh_auth_login>.

- Login with interactive prompt:

`gh auth login`

- Login with token from https://github.com/settings/tokens :

`echo {{your_token}} | gh auth login --with-token`

- Check if you are logged in:

`gh auth status`

- Log out:

`gh auth logout`

- Login to specific Github Enterprise Server:

`gh auth login --hostname {{enterprise.server.address}}`
