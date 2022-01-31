# usermod

> Modifica una conta d'usuari.
> Més informació: <https://manned.org/usermod>.

- Canvia el nom d'usuari:

`usermod -l {{nou_nom}} {{usuari}}`

- Afegeix un usuari a grups suplementaris (cal tenir en compte els espais en blanc):

`usermod -a -G {{grup1,grup2}} {{usuari}}`

- Crea un nou directori home per un usuari i mou tots els arxius a ell:

`usermod -m -d {{ruta/al/home}} {{usuari}}`
