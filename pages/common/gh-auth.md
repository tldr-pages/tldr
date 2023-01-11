# gh auth

> Authenticate with a GitHub host from the command-line.
> More information: <https://cli.github.com/manual/gh_auth>.

- Log in with interactive prompt:

`gh auth login`

- Log in with a token from standard input (created in https://github.com/settings/tokens):

`echo {{your_token}} | gh auth login --with-token`

- Check if you are logged in:

`gh auth status`

- Log out:

`gh auth logout`

- Log in with a specific GitHub Enterprise Server:

`gh auth login --hostname {{github.example.com}}`

- Refresh the session to ensure authentication credentials have the correct minimum scopes (removes additional scopes requested previously):

`gh auth refresh`

- Expand the permission scopes:

`gh auth refresh --scopes {{repo,admin:repo_hook,admin:org,admin:public_key,admin:org_hook,...}}`
