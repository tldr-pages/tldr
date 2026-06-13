# csshX

> Herramienta SSH de clúster para macOS.
> Más información: <https://github.com/brockgr/csshx>.

- Conectarse a múltiples hosts:

`csshX {{nombrehost1}} {{nombrehost2}}`

- Conectarse a múltiples hosts con una clave SSH dada:

`csshX {{usuario@nombrehost1}} {{usuario@nombrehost2}} --ssh_args "-i {{ruta/al/archivo_de_clave.pem}}"`

- Conectarse a un clúster predefinido desde `/etc/clusters`:

`csshX cluster1`
