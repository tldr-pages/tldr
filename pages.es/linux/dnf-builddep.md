# dnf builddep

> Instala dependencias para construir un paquete dado.
> No está predeterminado en `dnf` pero está soportado a través de `dnf-plugins-core`.
> Vea también: `dnf`.
> Más información: <https://dnf-plugins-core.readthedocs.io/en/latest/builddep.html>.

- Instala dependencias para un paquete dado:

`dnf builddep {{ruta/a/especificacion.spec}}`

- Instala dependencias para un paquete dado pero ignora los no disponibles:

`dnf builddep --skip-unavailable {{ruta/a/especificacion.spec}}`

- Define la macro RPM a una expresión dada:

`dnf builddep {{[-D|--define]}} '{{expresión}}'`

- Define un argumento para una ruta de archivo `.spec`:

`dnf builddep --spec {{argumento}}`

- Define un argumento para una ruta de archivo `.rpm`:

`dnf builddep --srpm {{argumento}}`

- Muestra la ayuda:

`dnf builddep --help-cmd`
