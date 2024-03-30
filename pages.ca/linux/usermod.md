# usermod

> Modifica una conta d'usuari.
> Vegeu també: `users`, `useradd`, `userdel`.
> Més informació: <https://manned.org/usermod>.

- Canvia el nom d'usuari:

`sudo usermod --login {{nou_nom_usuari}} {{nom_usuari}}`

- Canvia l'id d'usuari:

`sudo usermod --uid {{id}} {{nom_usuari}}`

- Canvia la shell d'un usuari:

`sudo usermod --shell {{cami/a/shell}} {{nom_usuar}}`

- Afegeix un usuari a grups suplementaris (cal tenir en compte els espais en blanc):

`sudo usermod --append --groups {{grup1,grup2}} {{nom_usuar}}`

- Crea un nou directori home per un usuari i mou tots els arxius a ell:

`sudo usermod --move-home --home {{ruta/al/home}} {{nom_usuar}}`
