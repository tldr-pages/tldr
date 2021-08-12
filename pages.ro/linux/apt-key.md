# apt-key

> Utilitar de gestionare a cheilor pentru APT Package Manager pe Debian și Ubuntu.
> Notă: `apt-key` este acum învechit (cu excepția utilizării `apt-key del` în scripturile de întreținere).
> Mai multe informaţii: <https://manpages.debian.org/latest/apt/apt-key.8.html>

- Lista cheilor de încredere:

`apt-key list`

- Adăugați o cheie la magazinul de chei de încredere:

`apt-key add {{public_key_file.asc}}`

- Ștergeți o cheie din magazinul de chei de încredere:

`apt-key del {{key_id}}`

- Adăugați o cheie de la distanță la magazinul de chei de încredere:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- Adăugați o cheie de la keyserver cu numai ID cheie:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
