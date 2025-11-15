# emacsclient

> Abre archivos en un servidor Emacs existente.
> Vea también `emacs`.
> Más información: <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>.

- Abre un archivo en un servidor Emacs existente (utilizando GUI si está disponible):

`emacsclient {{ruta/al/archivo}}`

- Abre un archivo en modo consola (sin una ventana X):

`emacsclient --no-window-system {{ruta/al/archivo}}`

- Abre un archivo en una nueva ventana Emacs:

`emacsclient --create-frame {{ruta/al/archivo}}`

- Evalúa un comando, imprime la salida a `stdout`, y luego sale:

`emacsclient --eval '({{comando}})'`

- Especifica un editor alternativo en caso de que ningún servidor Emacs esté funcionando:

`emacsclient --alternate-editor {{editor}} {{ruta/al/archivo}}`

- Detiene un servidor Emacs en funcionamiento y todas sus instancias, pidiendo confirmación en archivos no guardados:

`emacsclient --eval '(save-buffers-kill-emacs)'`
