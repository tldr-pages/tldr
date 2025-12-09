# zenity

> Muestra diálogos desde guiones de la línea de comandos.
> Regresa los valores suministrados por el usuario o 1 si hay error.
> Más información: <https://manned.org/zenity>.

- Muestra el diálogo predeterminado de pregunta:

`zenity --question`

- Muestra un diálogo de información que muestra el texto "¡Hola!":

`zenity --info --text="{{¡Hola!}}"`

- Muestra un formulario de nombre/contraseña y retorna los datos separados por ";":

`zenity --forms --add-entry="{{Nombre}}" --add-password="{{Contraseña}}" --separator="{{;}}"`

- Muestra un formulario de selección de archivos en el que el usuario sólo puede seleccionar directorios:

`zenity --file-selection --directory`

- Muestra una barra de progreso que actualiza su mensaje cada segundo y muestra un porcentaje de progreso:

`{{(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")}} | zenity --progress`
