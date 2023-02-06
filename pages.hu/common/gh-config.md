# gh config

> Konfiguráció módosítása a GitHub cli számára. További információ: <https://cli.github.com/manual/gh_config>.

- Megjeleníti, hogy milyen Git protokollt használ:

`gh config get git_protocol`

- SSH protokollt állítson be:

`gh config set git_protocol {{ssh}}`

- Használja a `delta` oldalsó üzemmódban az összes `gh` parancs alapértelmezett lapozójaként:

`gh config set pager '{{delta --side-by-side}}'`

- Állítsa be a szövegszerkesztőt Vim-re:

`gh config set editor {{vim}}`

- Alapértelmezett szövegszerkesztőre való visszaállítás:

`gh config set editor {{""}}`

- Interaktív kérések kikapcsolása:

`gh config set prompt {{disabled}}`

- Egy adott konfigurációs érték beállítása:

`gh config set {{key}} {{value}}`
