# delta

> Un visor para Git y salida diff.
> Vea también: `diff`, `difft`.
> Más información: <https://dandavison.github.io/delta/full---help-output.html>.

- Compara archivos o directorios:

`delta {{ruta/al/archivo_antiguo_o_directorio}} {{ruta/al/archivo_o_directorio_nuevo}}`

- Compara archivos o directorios, mostrando los números de línea:

`delta {{[-n|--line-numbers]}} {{ruta/al/archivo_o_directorio_antiguo}} {{ruta/al/archivo_o_directorio_nuevo}}`

- Compara archivos o directorios, mostrando las diferencias una al lado de la otra:

`delta {{[-s|--side-by-side]}} {{ruta/al/archivo_o_directorio_antiguo}} {{ruta/al/archivo_o_directorio_nuevo}}`

- Compara archivos o directorios, ignorando cualquier configuración de Git:

`delta --no-gitconfig {{ruta/al/archivo_o_directorio_antiguo}} {{ruta/al/archivo_o_directorio_nuevo}}`

- Compara, mostrando los hash de las confirmaciones, los nombres de los archivos y los números de línea como hipervínculos, de acuerdo con la especificación de hipervínculos para emuladores de terminal:

`delta --hyperlinks {{ruta/al/archivo_o_directorio_antiguo}} {{ruta/al/archivo_o_directorio_nuevo}}`

- Muestra la configuración actual:

`delta --show-config`

- Muestra los idiomas compatibles y las extensiones de archivo asociadas:

`delta --list-languages`
