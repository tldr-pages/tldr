# figlet

> Genera encabezados usando caracteres ASCII desde la entrada del usuario.
> Véase también `showfigfonts`.
> Más información: <http://www.figlet.org/figlet-man.html>.

- Genera el encabezado directamente introduciendo el texto:

`figlet {{texto_de_entrada}}`

- Usa un archivo de fuente personalizada:

`figlet {{texto_de_entrada}} -f {{ruta/al/archivo_de_fuente.flf}}`

- Use una fuente del directorio predeterminado (la extensión puede ser omitida):

`figlet {{texto_de_entrada}} -f {{archivo_de_fuente}}`

- Redirige la salida de un comando hacia figlet:

`{{comando}} | figlet`
