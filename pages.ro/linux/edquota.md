# edquota

> Editare cote pentru un utilizator sau grup. Implicit funcționează pe toate sistemele de fișiere cu cote.
> Informațiile despre cotă sunt stocate permanent în fișierele `quota.user` și `quota.group` din rădăcina sistemului de fișiere.
> Mai multe informaţii: <https://manned.org/edquota>

- Editează cota utilizatorului curent:

`edquota --user $(whoami)`

- Editarea cotei unui anumit utilizator:

`sudo edquota --user {{username}}`

- Editarea cotei pentru un grup:

`sudo edquota --group {{group}}`

- Restricționarea operațiunilor la un anumit sistem de fișiere (în mod implicit edquota funcționează pe toate sistemele de fișiere cu cote):

`sudo edquota --file-system {{filesystem}}`

- Editați perioada de grație implicită:

`sudo edquota -t`

- Duplicarea unei cote altor utilizatori:

`sudo edquota -p {{reference_user}} {{destination_user1}} {{destination_user2}}`
