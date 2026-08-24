# jj config get

> Get the value of a given config option.
> Unlike `jj config list`, the result is printed without extra formatting for use in scripts.
> See also: `jj config list`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-config-get>.

- Get the value of a config option:

`jj config {{[g|get]}} {{name}}`

- Get the configured user name:

`jj config {{[g|get]}} user.name`

- Get the configured user email:

`jj config {{[g|get]}} user.email`

- Get the default revset for the log command:

`jj config {{[g|get]}} revsets.log`
