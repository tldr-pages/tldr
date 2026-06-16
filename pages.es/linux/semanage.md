# semanage

> Herramienta de gestión de políticas persistentes de SELinux.
> Algunos subcomandos, como `boolean`, `fcontext`, `port`, etc., tienen su propia documentación de uso.
> Más información: <https://manned.org/semanage>.

- Establece o desactiva un booleano de SELinux. Los booleanos permiten al administrador personalizar cómo las reglas de política afectan a los tipos de procesos confinados (también conocidos como dominios):

`sudo semanage boolean {{[-m|--modify]}} {{--on|--off}} {{haproxy_connect_any}}`

- Añade una regla de etiquetado de contexto de archivo definida por el usuario. Los contextos de archivo definen a qué archivos pueden acceder los dominios confinados:

`sudo semanage fcontext {{[-a|--add]}} {{[-t|--type]}} {{samba_share_t}} '/mnt/share(/.*)?'`

- Añade una regla de etiquetado de puertos definida por el usuario. Las etiquetas de puerto definen en qué puertos se permite que los dominios confinados escuchen:

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{ssh_port_t}} {{[-p|--proto]}} {{tcp}} {{22000}}`

- Activa o desactiva el modo permisivo para un dominio confinado. El modo permisivo por dominio permite un control más granular en comparación con `setenforce`:

`sudo semanage permissive {{--add|--delete}} {{httpd_t}}`

- Muestra las personalizaciones locales en el almacén predeterminado:

`sudo semanage export {{[-f|--output_file]}} {{ruta/al/archivo}}`

- Importa un archivo generado por `semanage export` a las personalizaciones locales (¡ATENCIÓN: puede eliminar las personalizaciones actuales!):

`sudo semanage import {{[-f|--input_file]}} {{ruta/al/archivo}}`
