# yadm-gitconfig

> Pass options to `git config`. Change the `.gitconfig` of the repository managed by `yadm`.
> See also: `git config`.
> More information: <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#commands>.

- Update or set a Git configuration value:

`yadm gitconfig {{key.inner-key}} {{value}}`

- Get a value from `yadm`'s Git configuration:

`yadm gitconfig --get {{key}}`

- Unset a value in `yadm`'s Git configuration:

`yadm gitconfig --unset {{key}}`

- List all values in `yadm`'s Git configuration:

`yadm gitconfig --list`
