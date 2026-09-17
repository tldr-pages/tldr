# gh skyline

> Genera un modelo 3D de tu historial de contribuciones a GitHub.
> Por defecto, creará un archivo `{usuario}-{año}-github-skyline.stl` en el directorio actual.
> Más información: <https://github.com/github/gh-skyline>.

- Genera un archivo STL de la línea del horizonte para el año actual y el usuario autenticado:

`gh skyline`

- Genera una línea del horizonte para un [u]suario y un año [y] específicos:

`gh skyline {{[-u|--user]}} {{nombre_de_usuario}} {{[-y|--year]}} {{año}}`

- Genera una línea del horizonte para un intervalo de [a]ños:

`gh skyline {{[-u|--user]}} {{nombre_de_usuario}} {{[-y|--year]}} {{primer_año}}-{{último_año}}`

- Genera una línea del horizonte completa [f] (desde el año de alta del usuario hasta el año actual):

`gh skyline {{[-u|--user]}} {{nombre_de_usuario}} {{[-f|--full]}}`

- Habilita el registro de [d]epuración:

`gh skyline {{[-d|--debug]}}`

- Genera una línea del horizonte y especifica la ruta del archivo de salida:

`gh skyline {{[-o|--output]}} {{ruta/al/archivo_salida.stl}}`

- Abre el perfil de GitHub de un [u]suario específico:

`gh skyline {{[-u|--user]}} {{nombre_de_usuario}} {{[-w|--web]}}`

- Muestra ayuda:

`gh skyline {{[-h|--help]}}`
