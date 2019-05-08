# gopass

> Standard Unix Password Manager for Teams. Written in Go.

- Initialise the configuration settings:

`gopass init`

- Show all "keystores":

`gopass mounts`

- Mount a shared git "keystore":

`gopass mounts add keystore_name location_git_repo`

- Search interactively using a keyword:

`gopass show keyword`

- Search using a keyword:

`gopass find keyword`

- Sync all mounted "keystores":

`gopass sync`

- Show particular password entry:

`gopass keystore_name/directory01/dir02/email@email.com`

- Create a new entry:

`gopass new`
