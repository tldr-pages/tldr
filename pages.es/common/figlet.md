# figlet

> Genera encabezados usando caracteres ASCII desde la entrada del usuario.
> Véase también `showfigfonts`.
> Más información: <http://www.figlet.org/figlet-man.html>.

- Genera el encabezado directamente introduciendo el texto:

`figlet {{texto_de_entrada}}`

- Usa un archivo de [f]uente personalizada:

`figlet {{texto_de_entrada}} -f {{ruta/al/archivo_de_fuente.flf}}`

- Usa una [f]uente del directorio predeterminado (la extensión puede ser omitida):

`figlet {{texto_de_entrada}} -f {{archivo_de_fuente}}`

- Redirige la salida de un comando hacia FIGlet:

`{{comando}} | figlet`

- Muestra las fuentes de FIGlet disponibles:

`showfigfonts {{texto_opcional_para_mostrar}}`

- Utiliza el ancho total del [t]erminal y [c]entra el texto de entrada:

`figlet -t -c {{texto_de_entrada}}`

- Muestra todos los caracteres utilizando todo su ancho para evitar traslapes:

`figlet -W {{input_text}}`
