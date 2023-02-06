# gopass

> Standard Unix Password Manager for Teams. Go nyelven íródott. További információ: <https://www.gopass.pw>.

- A konfigurációs beállítások inicializálása:

`gopass init`

- Hozzon létre egy új bejegyzést:

`gopass new`

- Minden tároló megjelenítése:

`gopass mounts`

- Megosztott Git tároló csatlakoztatása:

`gopass mounts add {{store_name}} {{git_repo_url}}`

- Interaktív keresés kulcsszóval:

`gopass show {{keyword}}`

- Keresés kulcsszóval:

`gopass find {{keyword}}`

- Az összes csatlakoztatott tároló szinkronizálása:

`gopass sync`

- Egy adott jelszavas bejegyzés megjelenítése:

`gopass {{store_name|path/to/directory|email@email.com}}`
