# distrobox-export

> Exporta aplicaciones/servicios/binarios del contenedor al sistema operativo anfitrión. Vea también: `tldr distrobox`.
> Más información: <https://distrobox.it/usage/distrobox-export>.

- Exporta una aplicación del contenedor al anfitrión (la entrada de escritorio/ícono aparecerá en la lista de aplicaciones del sistema anfitrión):

`distrobox-export --app {{paquete}} --extra-flags "--foreground"`

- Exporta un binario del contenedor al anfitrión:

`distrobox-export --bin {{ruta/al/binario}} --export-path {{ruta/al/binario_en_anfitrión}}`

- Exporta un binario del contenedor al anfitrión (es decir, `$HOME/.local/bin`) :

`distrobox-export --bin {{ruta/al/binario}} --export-path {{ruta/a/exportar}}`

- Exporta un servicio desde el contenedor al anfitrión (`--sudo` ejecutará el servicio como root dentro del contenedor):

`distrobox-export --service {{paquete}} --extra-flags "--allow-newer-config" --sudo`

- Elimina o deja de exportar una aplicación exportada:

`distrobox-export --app {{paquete}} --delete`
