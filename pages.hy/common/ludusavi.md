#լյուդուսավի

> Կրկնօրինակեք վիդեո խաղերի տվյալները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mtkennerly/ludusavi/blob/master/docs/cli.md>:.

- Պահուստային խաղեր.:

`ludusavi backup --path {{path/to/backup}}`

- Վերականգնել խաղերը.:

`ludusavi restore --path {{path/to/backup}} {{"game1" "game2" ...}}`

- Ցանկի կրկնօրինակները.:

`ludusavi backups --path {{path/to/backup}}`

- Փաթաթել գործարկիչ խաղ.:

`ludusavi wrap --gui --infer {{heroic|lutris|steam}} -- {{game_launch_commands}}`

- Փաթեթավորեք ինքնուրույն խաղ.:

`ludusavi wrap --gui --name {{name}} -- {{game_launch_commands}}`
