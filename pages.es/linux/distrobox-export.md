# distrobox-export

> Exporta aplicaciones/servicios/binarios del contenedor al sistema operativo anfitrión.
> Vea también: `distrobox`.
> Más información: <https://distrobox.it/usage/distrobox-export/>.

- Exporta una aplicación del contenedor al anfitrión (la entrada de escritorio/ícono aparecerá en la lista de aplicaciones del sistema anfitrión):

`distrobox-export {{[-a|--app]}} {{paquete}} {{[-ef|--extra-flags]}} "--foreground"`

- Exporta un binario del contenedor al anfitrión:

`distrobox-export {{[-b|--bin]}} {{ruta/al/binario}} {{[-ep|--export-path]}} {{ruta/al/binario_en_anfitrión}}`

- Exporta un binario del contenedor al anfitrión (es decir, `$HOME/.local/bin`):

`distrobox-export {{[-b|--bin]}} {{ruta/al/binario}} {{[-ep|--export-path]}} {{ruta/a/exportar}}`

- Exporta un servicio desde el contenedor al anfitrión (`--sudo` ejecutará el servicio como root dentro del contenedor):

`distrobox-export --service {{paquete}} {{[-ef|--extra-flags]}} "--allow-newer-config" {{[-S|--sudo]}}`

- Elimina o deja de exportar una aplicación exportada:

`distrobox-export {{[-a|--app]}} {{paquete}} {{[-d|--delete]}}`
