# rig

> Utilidad para generar un nombre, apellidos y dirección consistente (por ej. calle, número, ciudad).
> Más información: <https://manpages.ubuntu.com/manpages/focal/man6/rig.6.html>.

- Mostrar un nombre aleatorio (masculino o femenino) y dirección:

`rig`

- Mostrar un nombre [m]asculino, (o [f]emenino) aleatorio y dirección:

`rig -{{m|f}}`

- Usar archivos de datos de un directorio específico (por defecto `/usr/share/rig`):

`rig -d {{ruta/al/directorio}}`

- Especificar el número de identidades a generar:

`rig -c {{número}}`

- Especificar el número de identidades femininas a generar:

`rig -f -c {{número}}`
