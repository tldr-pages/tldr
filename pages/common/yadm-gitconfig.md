# yadm-gitconfig

> Pass options to the git config command.
> This will be used to change the `.gitconfig` of the repo managed by `yadm`.
> More information: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>

- To update or set a git config value:

`yadm gitconfig <key.inner-key> {{value}}`

- To get a value from yadm's git config:

`yadm gitconfig --get {{key}}`

- To unset a value in yadm's git config:

`yadm gitconfig --unset {{key}}`

- To list all values in yadm's git config:

`yadm gitconfig --list`
