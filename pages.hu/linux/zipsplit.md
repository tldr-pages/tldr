# zipsplit

> Beolvas egy zip-fájlt, és kisebb zip-fájlokra osztja. További információ: <https://manned.org/zipsplit>.

- Zipfile felosztása olyan darabokra, amelyek nem nagyobbak egy adott méretnél \[n\]:

`zipsplit -n {{size}} {{path/to/archive.zip}}`

- \[p\]ause az egyes felosztott zipfile-ok létrehozása között:

`zipsplit -p -n {{size}} {{path/to/archive.zip}}`

- A felosztott zipfile-ok kimenete a `archive` könyvtárba:

`zipsplit -b {{archive}} -n {{size}} {{path/to/archive.zip}}`
