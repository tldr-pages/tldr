# bacon

> Un verificador de código en segundo plano para Rust.
> Más información: <https://github.com/Canop/bacon>.

- Ejecuta `cargo check` cada vez que se detecta un cambio en el directorio actual:

`bacon`

- Ejecuta `cargo test` siempre que se detecte un cambio en el directorio dado:

`bacon test {{ruta/a/directorio}}`

- Ejecuta `cargo check` contra todos los objetivos siempre que se detecte un cambio en el directorio actual:

`bacon check-all`

- Ejecuta un trabajo específico cada vez que se detecta un cambio en el directorio actual:

`bacon {{run|test|clippy|doc|...}}`

- Lista todos los trabajos disponibles:

`bacon --list-jobs`

- Inicializa un archivo de configuración `bacon.toml` en el directorio actual:

`bacon --init`
