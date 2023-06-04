# whence

> Un comando integrado de zsh para indicar cómo se interpretaría un comando dado.
> Más información: <https://www.unix.com/man-page/OpenSolaris/1/whence/>.

- Interpreta {{command}}, con expansión si se define como un `alias` (similar al `command -v` integrado):

`whence "{{command}}"`

- Muestra tipo de {{command}}, con localización si se define como una función, o binario (equivalente a los `type` y `command -V` integrados):

`whence -v "{{comando}}"`

- Igual que el anterior, excepto que muestra el contenido de las funciones del shell en lugar de la ubicación (equivalente al `which` integrado):

`whence -c "{{command}}"`

- Igual que el anterior, pero muestra todas las apariciones en la ruta del comando (equivalente al `where` integrado):

`whence -ca " {{command}}"`

- Buscar sólo el `PATH`para {{command}}, ignorando los buildins, aliases o funciones del shell (equivalente al comando `where`):

`whence -p "{{command}}"`
