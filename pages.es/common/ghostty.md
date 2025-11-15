# ghostty

> Un emulador de terminal rápido, rico en características y multiplataforma que utiliza UI nativa de la plataforma y aceleración GPU.
> Nota: todas las opciones del archivo de configuración también pueden utilizarse en la línea de comandos (utilizando `--option=argument`).
> Más información: <https://ghostty.org/docs/config/reference>.

- Abre una nueva ventana de Ghostty (no compatible con macOS):

`ghostty`

- Ejecuta un comando específico en una nueva ventana de Ghostty (no compatible con macOS):

`ghostty -e {{comando}}`

- Lista todas las combinaciones de teclas predeterminadas y configuradas:

`ghostty +list-keybinds`

- Lista todas las acciones (es decir, lo que se puede activar a través de combinaciones de teclas):

`ghostty +list-actions`

- Consulta una lista interactiva de temas:

`ghostty +list-themes`

- Imprime la configuración por defecto (incluidos los comentarios):

`ghostty +show-config --default --docs`
