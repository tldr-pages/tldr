# gh-config

> Change configuration for GitHub cli.
> More information: <https://cli.github.com/manual/gh_config>.

- Check what git protocol you are using:

`gh config get git_protocol`

- Change protocol to ssh:

`gh config set git_protocol ssh`

- Change text editor to vim:

`gh config set editor vim`

- Reset to default editor:

`gh config set editor ""`

- Disable interactive prompts:

`gh config set prompt disabled`
