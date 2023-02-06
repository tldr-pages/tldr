# ssh-add

> A betöltött ssh-kulcsok kezelése az ssh-agentben. Győződjön meg róla, hogy az ssh-agent működik, hogy a kulcsokat be lehessen tölteni. További információ: <https://man.openbsd.org/ssh-add>.

- Adja hozzá az alapértelmezett ssh-kulcsokat a `~/.ssh` oldalon az ssh-agenthez:

`ssh-add`

- Adjon hozzá egy adott kulcsot az ssh-agenthez:

`ssh-add {{path/to/private_key}}`

- A jelenleg betöltött kulcsok ujjlenyomatainak listázása:

`ssh-add -l`

- Kulcs törlése az ssh-agentből:

`ssh-add -d {{path/to/private_key}}`

- Az összes jelenleg betöltött kulcs törlése az ssh-agentből:

`ssh-add -D`

- Kulcs hozzáadása az ssh-agenthez és a kulcstárhoz:

`ssh-add -K {{path/to/private_key}}`
