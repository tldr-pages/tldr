# useradd

> Crea un nou usuari.
> Més informació: <https://manned.org/useradd>.

- Crea un usuari nou:

`useradd {{nom}}`

- Crea un usuari nou amb el directori home predeterminat:

`useradd --create-home {{nom}}`

- Crea un usuari nou amb una shell específica:

`useradd --shell {{ruta/a/la/shell}} {{nom}}`

- Crea un usuari nou pertanyent a grups adicionals (cal tenir en compte que no existeixen espais en blanc):

`useradd --groups {{grup1,grup2}} {{nom}}`

- Crea un usuari nou del sistema sense directori home:

`useradd --no-create-home --system {{nombre}}`
