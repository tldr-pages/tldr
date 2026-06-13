# cargo build

> Compila un paquete local y todas sus dependencias.
> Más información: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Construye el paquete o los paquetes definidos por el archivo manifiesto `Cargo.toml` en la ruta local:

`cargo {{[b|build]}}`

- Construye artefactos en modo de lanzamiento, con optimizaciones:

`cargo {{[b|build]}} {{[-r|--release]}}`

- Exige que `Cargo.lock` esté actualizado:

`cargo {{[b|build]}} --locked`

- Construye todos los paquetes en el espacio de trabajo:

`cargo {{[b|build]}} --workspace`

- Construye un paquete determinado:

`cargo {{[b|build]}} {{[-p|--package]}} {{paquete}}`

- Construye solo el binario especificado:

`cargo {{[b|build]}} --bin {{nombre}}`

- Construye solamente el objetivo de prueba especificado:

`cargo {{[b|build]}} --test {{nombre_de_la_prueba}}`
