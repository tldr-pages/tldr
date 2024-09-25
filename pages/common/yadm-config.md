# yadm-config

> Pass options to yadm's config file.
> This will be used to change the `.config` of the repo managed by `yadm`.
> Find out what you can change. <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#configuration>.

- Set or update a yadm's git config:

`yadm config <key.inner-key> {{value}}`

- Get a value from yadm's git config:

`yadm config --get {{key}}`

- Unset a value in yadm's git config:

`yadm config --unset {{key}}`

- List all values in yadm's git config:

`yadm config --list`
