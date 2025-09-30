# fwconsole

> Gestiona y configura un sistema FreePBX (servidor PBX).
> Más información: <https://sangomakb.atlassian.net/wiki/spaces/PG/pages/41779247/fwconsole+commands+13>.

- Recarga las configuraciones de FreePBX:

`fwconsole reload`

- Inicia Asterisk y otros comandos necesarios para FreePBX:

`fwconsole start`

- Detiene Asterisk y otros comandos necesarios para FreePBX:

`fwconsole stop`

- Visualiza y actualiza la configuración:

`fwconsole setting {{palabra_clave}} {{nuevo_valor}}`

- Lista las copias de seguridad disponibles:

`fwconsole backup --list`

- Lista de comandos FreePBX disponibles:

`fwconsole list`

- Cambia la propiedad de todos los archivos y directorios que FreePBX necesita que sean propiedad del usuario apache:

`fwconsole chown`
