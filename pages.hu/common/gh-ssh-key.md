# gh ssh-key

> A GitHub SSH-kulcsok kezelése a parancssorból. További információk: <https://cli.github.com/manual/gh_ssh-key>.

- Súgó megjelenítése:

`gh ssh-key`

- Az aktuálisan hitelesített felhasználó SSH-kulcsainak listázása:

`gh ssh-key list`

- SSH-kulcs hozzáadása az aktuálisan hitelesített felhasználó fiókjához:

`gh ssh-key add {{path/to/key.pub}}`

- SSH-kulcs hozzáadása az aktuálisan hitelesített felhasználó fiókjához egy adott címmel:

`gh ssh-key add --title {{title}} {{path/to/key.pub}}`
