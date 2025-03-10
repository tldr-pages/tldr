# crane copy

> Copia eficientemente una imagen remota de origen a destino conservando el valor de resumen.
> Más información: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- Copia una imagen de origen a destino:

`crane copy {{origen}} {{destino}}`

- Copia todas las etiquetas:

`crane copy {{origen}} {{destino}} {{[-a|--all-tags]}}`

- Establece el número máximo de copias simultáneas, predeterminados a GOMAXPROCS:

`crane copy {{origen}} {{destino}} {{[-j|--jobs]}} {{número}}`

- Evita sobrescribir las etiquetas existentes en el destino:

`crane copy {{origen}} {{destino}} {{[-n|--no-clobber]}}`

- Muestra la ayuda:

`crane copy {{[-h|--help]}}`
