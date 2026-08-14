# rustup toolchain

> Gestiona las cadenas de herramientas de Rust.
> Consulta `rustup help toolchain` para obtener más información sobre las cadenas de herramientas.
> Más información: <https://rust-lang.github.io/rustup/>.

- Instala o actualiza una cadena de herramientas concreta:

`rustup toolchain install {{cadena_de_herramientas}}`

- Desinstala una cadena de herramientas:

`rustup toolchain uninstall {{cadena_de_herramientas}}`

- Muestra una lista de las cadenas de herramientas instaladas:

`rustup toolchain list`

- Crea una cadena de herramientas personalizada mediante un enlace simbólico a un directorio:

`rustup toolchain link {{nombre_de_la_cadena_de_herramientas_personalizada}} {{ruta/al/directorio}}`
