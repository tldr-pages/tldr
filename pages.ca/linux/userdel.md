# userdel

> Elimina una conta d'usuari o elimina un usuari d'un grup.
> Nota: tots els comandaments han de ser executats com a root.
> Més informació: <https://manned.org/userdel>.

- Elimina un usuari:

`userdel {{nom}}`

- Elimina un usuari en conjunt amb el seu directori home i mail spool:

`userdel --remove {{nom}}`

- Elimina un usuari d'un grup:

`userdel {{nom}} {{grup}}`

- Elimina un usuari en un altre directori root:

`userdel --root {{ruta/al/altre/root}} {{nom}}`
