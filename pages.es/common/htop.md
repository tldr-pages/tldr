# htop

> Muestra información dinámica en tiempo real sobre los procesos ejecutándose. Una versión mejorada de `top`.
> Más información: <https://manned.org/htop>.

- Inicia `htop`:

`htop`

- Inicia `htop` mostrando solo los procesos pertenecientes a un usuario dado:

`htop {{[-u|--user]}} {{usuario}}`

- Muestra procesos jerárquicamente en una vista de árbol para visibilizar las relaciones entre padres e hijos:

`htop {{[-t|--tree]}}`

- Ordena procesos especificando un `criterio_de_ordenamiento` (usa `htop --sort help` para ver las opciones disponibles):

`htop {{[-s|--sort]}} {{criterio_de_ordenamiento}}`

- Inicia `htop` con una espera dada entre las actualizaciones, en décimas de segundo (es decir, 50 = 5 segundos):

`htop {{[-d|--delay]}} {{50}}`

- Muestra comandos interactivos mientras se está ejecutando `htop`:

`<?>`

- Cambia a otro panel:

`<Tab>`

- Muestra la ayuda:

`htop {{[-h|--help]}}`
