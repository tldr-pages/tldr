# slapt-src

> Un utilitar pentru a automatiza construirea de slackbuilds.
> Sursele SlackBuild trebuie să fie configurate în fișierul slapt-srcrc.
> Mai multe informaţii: <https://github.com/jaos/slapt-src>

- Actualizați lista de slackbuilds și versiuni disponibile:

`slapt-src --update`

- Listează toate slackbuild-urile disponibile:

`slapt-src --list`

- Fetch, construi și instala slackbuild (s) specificat (e):

`slapt-src --install {{slackbuild_name}}`

- Localizați slackbuilds de interes după numele sau descrierea lor:

`slapt-src --search {{search_term}}`

- Afișează informații despre un slackbuild:

`slapt-src --show {{slackbuild_name}}`
