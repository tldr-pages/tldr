# eix

> Utilităţi pentru căutarea pachetelor locale Gentoo.
> Actualizați memoria cache a pachetelor locale utilizând `eix-update`.
> Mai multe informaţii: <https://wiki.gentoo.org/wiki/Eix>

- Caută un pachet:

`eix {{package_name}}`

- Caută pachete instalate:

`eix --installed {{package_name}}`

- Căutare în descrierile pachetelor:

`eix --description "{{description}}"`

- Căutare după licență pachet:

`eix --license {{license}}`

- Excludeți rezultatele din căutare:

`eix --not --license {{license}}`
