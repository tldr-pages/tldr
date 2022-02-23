# usermod

> Modifica una conta d'usuari.
> Vegeu també: `users`, `useradd`, `userdel`.
> Més informació: <https://manned.org/usermod>.

- Canvia el nom d'usuari:

`sudo_usermod -l {{nou_nom_usuari}} {{nom_usuari}}`

- Canvia l'id d'usuari:

`sudo_usermod --uid {{id}} {{nom_usuari}}`

- Canvia la shell d'un usuari:

`sudo_usermod --shell {{cami/a/shell}} {{nom_usuar}}`

- Afegeix un usuari a grups suplementaris (cal tenir en compte els espais en blanc):

`sudo_usermod -a -G {{grup1,grup2}} {{nom_usuar}}`

- Crea un nou directori home per un usuari i mou tots els arxius a ell:

`sudo_usermod -m -d {{ruta/al/home}} {{nom_usuar}}`
