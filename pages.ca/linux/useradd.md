# useradd

> Crea un nou usuari.
> Vegeu també: `users`, `userdel`, `usermod`.
> Més informació: <https://manned.org/useradd>.

- Crea un usuari nou:

`sudo useradd {{nom_usuari}}`

- Crea un usuari amb l'id d'usuari especificada:

`sudo useradd --uid {{id}} {{nom_usuari}}`

- Crea un usuari nou amb una shell específica:

`sudo useradd --shell {{ruta/a/la/shell}} {{nom_usuari}}`

- Crea un usuari nou pertanyent a grups adicionals (cal tenir en compte que no existeixen espais en blanc):

`sudo useradd --groups {{grup1,grup2}} {{nom_usuari}}`

- Crea un usuari nou amb el directori home predeterminat:

`sudo useradd --create-home {{nom_usuari}}`

- Crea un usuari nou amb el directori home omplert per una plantilla:

`sudo useradd --skel {{/cami/al/directori_plantilles}} --create-home {{nom_usuari}}`

- Crea un usuari nou del sistema sense directori home:

`sudo useradd --no-create-home --system {{nom_usuari}}`
