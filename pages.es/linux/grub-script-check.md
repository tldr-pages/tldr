# grub-script-check

> El programa `grub-script-check` toma un archivo de script de GRUB y lo verifica en busca de errores de sintaxis.
> Puede tomar una ruta como argumento no opcional. Si no se proporciona ninguna, lee desde `stdin`.
> Más información: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dscript_002dcheck>.

- Verifica un archivo de script específico en busca de errores de sintaxis:

`grub-script-check {{ruta/al/archivo_config_grub}}`

- Muestra cada línea de entrada después de leerla:

`grub-script-check {{[-v|--verbose]}}`

- Muestra la ayuda:

`grub-script-check --help`

- Muestra la versión:

`grub-script-check --version`
