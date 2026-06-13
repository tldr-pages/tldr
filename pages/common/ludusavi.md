# ludusavi

> Backup video game save data.
> More information: <https://github.com/mtkennerly/ludusavi/blob/master/docs/cli.md>.

- Backup games:

`ludusavi backup --path {{path/to/backup}}`

- Restore games:

`ludusavi restore --path {{path/to/backup}} {{"game1" "game2" ...}}`

- List backups:

`ludusavi backups --path {{path/to/backup}}`

- Wrap launcher game:

`ludusavi wrap --gui --infer {{heroic|lutris|steam}} -- {{game_launch_commands}}`

- Wrap standalone game:

`ludusavi wrap --gui --name {{name}} -- {{game_launch_commands}}`
