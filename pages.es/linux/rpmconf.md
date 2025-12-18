# rpmconf

> Gestiona los archivos RPMNEW, RPMSAVE y RPMORIG creados por las actualizaciones de paquetes.
> Vea también: `rpm`.
> Más información: <https://manned.org/rpmconf.8>.

- Lista los archivos sobrantes y elige interactivamente que hacer con cada uno de ellos:

`sudo rpmconf --all`

- Elimina los archivos huérfanos RPMNEW y RPMSAVE:

`sudo rpmconf --all --clean`
