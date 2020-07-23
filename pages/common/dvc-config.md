# dvc config

> Low level command to manage custom configuration options for dvc repositories.
> These configurations can be project/local/global/system level.
> More information: <https://dvc.org/doc/command-reference/config>.

- Get default remote name:

`dvc config core.remote`

- Set project default remote:

`dvc config core.remote {{remote_name}}`

- Unset project default remote:

`dvc config --unset core.remote`

- Get project config value for a key:

`dvc config key`

- Set project level config value for a key:

`dvc config key value`

- Unset project level config value for a key:

`dvc config --unset key`

- Set local/global/system level config:

`dvc config --local/global/system key value`
