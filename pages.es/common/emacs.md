# emacs

> El editor extensible, personalizable, autodocumentado, en tiempo real.
> Véase también `emacsclient`.
> Más información: <https://www.gnu.org/software/emacs>.

- Inicia Emacs y abre un archivo:

`emacs {{ruta/al/archivo}}`

- Abre un archivo en un número de línea especificado:

`emacs +{{line_number}} {{ruta/al/archivo}}`

- Ejecuta un archivo Emacs Lisp como guión (script):

`emacs --script {{ruta/al/archivo.el}}`

- Inicia Emacs en modo consola (sin una ventana X):

`emacs {{[-nw|--no-window-system]}}`

- Inicia un servidor Emacs en segundo plano (accesible a través de `emacsclient`):

`emacs --daemon`

- Detiene un servidor Emacs en funcionamiento y todas sus instancias, pidiendo confirmación en archivos no guardados:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Guarda un archivo en Emacs:

`<Ctrl x><Ctrl s>`

- Sale de Emacs:

`<Ctrl x><Ctrl c>`
