# etckeeper

> Urmăriți fișierele de configurare a sistemului în Git.
> Mai multe informaţii: <http://etckeeper.branchable.com/>

- Configurați un repo Git și efectuați diverse sarcini de configurare (executați de la `/etc`):

`sudo etckeeper init`

- Comite toate modificările în `/etc`:

`sudo etckeeper commit {{message}}`

- Rulați comenzi arbitrare Git:

`sudo etckeeper vcs {{status}}`

- Verificați dacă există modificări necomise (returnează doar un cod de ieșire):

`sudo etckeeper unclean`

- Distruge repo existente și opriți urmărirea modificărilor:

`sudo etckeeper uninit`
