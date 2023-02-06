# gitmoji

> Interaktív parancssori eszköz emojik használatára a commitokon. További információ: <https://github.com/carloscuesta/gitmoji-cli>.

- Indítsa el a commit varázslót:

`gitmoji --commit`

- Inicializálja a git hookot (így a `gitmoji` minden alkalommal lefut, amikor a `git commit` fut):

`gitmoji --init`

- Távolítsa el a git hookot:

`gitmoji --remove`

- Listázza ki az összes elérhető emojit és leírásukat:

`gitmoji --list`

- Keresés az emojik listáján a kulcsszavak listájára:

`gitmoji --search {{keyword1}} {{keyword2}}`

- Az emojik gyorsítótárazott listájának frissítése a fő adattárból:

`gitmoji --update`

- Globális beállítások konfigurálása:

`gitmoji --config`
