# cargo build

> Compila un paquete local y todas sus dependencias.
> Más información: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Construye el paquete o los paquetes definidos por el archivo manifiesto `Cargo.toml` en la ruta local:

`cargo build`

- Construye artefactos en modo de lanzamiento, con optimizaciones:

`cargo build --release`

- Exige que `Cargo.lock` esté actualizado:

`cargo build --locked`

- Construye todos los paquetes en el espacio de trabajo:

`cargo build --workspace`

- Construye un paquete en específico:

`cargo build --package {{paquete}}`

- Construye solo el binario especificado:

`cargo build --bin {{nombre}}`

- Construye solamente el objetivo de prueba especificado:

`cargo build --test {{nombre_de_la_prueba}}`
