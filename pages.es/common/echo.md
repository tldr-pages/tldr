# echo

> Imprime los argumentos dados.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Imprime un mensaje de texto. Nota: las comillas son opcionales:

`echo "{{Hola Mundo}}"`

- Imprime un mensaje con variables de ambiente:

`echo "{{Mi ruta es $PATH}}"`

- Imprime un mensaje sin la nueva línea:

`echo -n "{{Hola Mundo}}"`

- Añade un mensaje al final del archivo:

`echo "{{Hola Mundo}}" >> {{archivo.txt}}`

- Habilita la interpretación de escapes de backslash (caracteres especiales):

`echo -e "{{Column 1\tColumn 2}}"`

- Imprime el estado de salida del último comando ejecutado (Nota: En Windows Command Prompt y PowerShell los equivalentes son `echo %errorlevel%` y `$lastexitcode` respectivamente):

`echo $?`
