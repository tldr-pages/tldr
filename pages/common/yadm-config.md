# yadm-config

> Pass options to yadm's config file.
> This will be used to change the `.config` of the repo managed by `yadm`.
> To find out what you can change. <https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#configuration>.

- To set or update a yadm's git config:

`yadm config <key.inner-key> {{value}}`

- To get a value from yadm's git config:

`yadm config --get {{key}}`

- To unset a value in yadm's git config:

`yadm config --unset {{key}}`

- To list all values in yadm's git config:

`yadm config --list`
