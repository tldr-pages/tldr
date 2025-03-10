# userdel

> Elimina una conta d'usuari o elimina un usuari d'un grup.
> Vegeu també: `users`, `useradd`, `usermod`.
> Més informació: <https://manned.org/userdel>.

- Elimina un usuari:

`sudo userdel {{nom_usuari}}`

- Elimina un usuari en un altre directori root:

`sudo userdel {{[-R|--root]}} {{ruta/al/altre/root}} {{nom_usuari}}`

- Elimina un usuari en conjunt amb el seu directori home i mail spool:

`sudo userdel {{[-r|--remove]}} {{nom_usuari}}`
