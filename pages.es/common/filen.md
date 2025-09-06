# filen

> Interfaz con Filen, un servicio de almacenamiento en la nube cifrado de extremo a extremo.
> Más información: <https://github.com/FilenCloudDienste/filen-cli>.

- Entra en modo interactivo:

`filen`

- Sube un archivo local a una carpeta remota específica:

`filen upload {{ruta/al/archivo_local}} {{id_carpeta_remota}}`

- Descarga un archivo o carpeta utilizando su ID remoto:

`filen download {{id_remoto}} {{ruta/a/destino_local}}`

- Lista archivos y carpetas dentro de una carpeta remota:

`filen ls {{carpeta_remota}}`

- Elimina un archivo o carpeta remoto (lo mueve a la papelera):

`filen rm {{id_remoto}}`

- Restaura un elemento de la papelera:

`filen trash restore {{id_remoto}}`

- Sincroniza una carpeta local con una carpeta remota (sincronización bidireccional):

`filen sync {{ruta/a/carpeta_local}}:/{{carpeta_remota}} --continuous`

- Descarga los cambios desde la nube a una carpeta local (sincronización unidireccional):

`filen sync {{ruta/a/carpeta_local}}:ctl:/{{carpeta_remota}}`
