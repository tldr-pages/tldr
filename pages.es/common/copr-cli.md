# copr-cli

> Interfaz con la instancia copr de Fedora-Projects para construir RPMs y publicarlos.
> Más información: <https://manned.org/copr-cli>.

- Muestra al usuario conectado a copr:

`copr-cli whoami`

- Genera un archivo spec local en copr:

`copr-cli build {{repositorio}} {{ruta/al/archivo_de_especificaciones}}`

- Comprueba el estado de las compilaciones:

`copr-cli list-builds {{repositorio}}`

- Activa una compilación copr de un archivo de especificaciones desde un repositorio público (Git):

`copr-cli buildscm {{repositorio}} --clone-url {{https://git.example.org/repo}} --spec {{nombre_archivo_espec}}`
