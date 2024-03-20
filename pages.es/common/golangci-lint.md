# golangci-lint

> Corredor de linters Go paralelizado, inteligente y rápido que se integra con los principales entornos de desarrollo integrado y soporta configuración en YAML.
> Más información: <https://golangci-lint.run/usage/quick-start/>.

- Ejecuta linters en la carpeta actual:

`golangci-lint run`

- Lista los linters habilitados y deshabilitados (Nota: los linters deshabilitados se muestran en el último lugar, no los confundas con los habilitados):

`golangci-lint linters`

- Habilita un linter específico para esta ejecución:

`golangci-lint run --enable {{linter}}`
