# semanage fcontext

> Gestiona las reglas persistentes del contexto de seguridad de SELinux en archivos y directorios.
> Vea también: `semanage`, `matchpathcon`, `secon`, `chcon`, `restorecon`.
> Más información: <https://manned.org/semanage-fcontext>.

- Muestra todas las reglas de etiquetado de archivos:

`sudo semanage fcontext {{[-l|--list]}}`

- Muestra todas las reglas de etiquetado de archivos definidas por el usuario sin encabezados:

`sudo semanage fcontext {{[-lCn|--list --locallist --noheading]}}`

- Añade una regla definida por el usuario que etiquete cualquier ruta que coincida con una `expresión regular` PCRE:

`sudo semanage fcontext {{[-a|--add]}} {{[-t|--type]}} {{samba_share_t}} '{{/mnt/share(/.*)?}}'`

- Añade una regla definida por el usuario que establezca una equivalencia de etiquetado entre dos subrutas:

`sudo semanage fcontext {{[-a|--add]}} {{[-e|--equal]}} /{{ruta/a/ref}} /{{ruta/a/target}}`

- Elimina una regla definida por el usuario utilizando su expresión regular PCRE:

`sudo semanage fcontext {{[-d|--delete]}} '{{/mnt/share(/.*)?}}'`

- Reetiqueta un directorio de forma recursiva aplicando las nuevas reglas:

`restorecon -Rv {{ruta/al/directorio}}`
