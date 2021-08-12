# pio package

> Gestionați pachetele din registry.
> Pachetele pot fi eliminate numai în termen de 72 de ore (3 zile) de la data publicării lor.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/package/>

- Creați un pachet de tarball din directorul curent:

`pio package pack --output {{path/to/package.tar.gz}}`

- Creați și publicați un pachet de tarball din directorul curent:

`pio package publish`

- Publicați directorul curent și restricționați accesul public la acesta:

`pio package publish --private`

- Publicarea unui pachet:

`pio package publish {{path/to/package.tar.gz}}`

- Publicarea unui pachet cu o dată de lansare particularizată (UTC):

`pio package publish {{path/to/package.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- Eliminați toate versiunile unui pachet publicat din registru:

`pio package unpublish {{package_name}}`

- Eliminați o versiune specifică a unui pachet publicat din registru:

`pio package unpublish {{package_name}}@{{version}}`

- Anulați eliminarea, punând toate versiunile sau o versiune specifică a pachetului înapoi în registru:

`pio package unpublish --undo {{package_name}}@{{version}}`
