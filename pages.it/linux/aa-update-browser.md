# aa-update-browser

> Aggiorna i profili browser di AppArmor per utilizzare le astrazioni supportate.
> Parte della suite AppArmor.
> Maggiori informazioni: <https://manned.org/aa-update-browser>.

- [l]ista i profili di astrazione browser disponibili:

`sudo aa-update-browser -l`

- Mostra quali modifiche verrebbero apportate a un profilo senza applicarle (simulazione):

`sudo aa-update-browser -d {{path/to/profile}}`

- [a]ggiorna un profilo con astrazioni specifiche:

`sudo aa-update-browser -u {{astrazione1,astrazione2,...}} {{path/to/profile}}`

- Rimuove tutte le astrazioni da un profilo:

`sudo aa-update-browser -u '' {{path/to/profile}}`

- Mostra aiuto:

`aa-update-browser -h`
