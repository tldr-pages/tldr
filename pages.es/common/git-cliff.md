# git cliff

> Un generador de registros de cambios altamente personalizable.
> Más información: <https://git-cliff.org/docs/usage/args>.

- Genera un registro de cambios a partir de todos los commits de un repositorio Git y lo guarda en `CHANGELOG.md`:

`git cliff > {{CHANGELOG.md}}`

- Genera un registro de cambios a partir de las confirmaciones desde la última etiqueta y lo imprime en `stdout`:

`git cliff {{[-l|--latest]}}`

- Genera un registro de cambios a partir de las confirmaciones que pertenecen a la etiqueta actual (usa `git checkout` en una etiqueta anterior a esta):

`git cliff --current`

- Genera un registro de cambios a partir de las confirmaciones que no pertenecen a una etiqueta:

`git cliff {{[-u|--unreleased]}}`

- Escribe el archivo de configuración por defecto en `cliff.toml` en el directorio actual:

`git cliff {{[-i|--init]}}`
