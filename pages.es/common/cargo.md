# cargo

> Gestiona proyectos Rust y sus dependencias de módulos (crates).
> Algunos subcomandos como `build` tienen su propia documentación de uso.
> Más información: <https://doc.rust-lang.org/cargo>.

- Busca crates:

`cargo search {{cadena_de_busqueda}}`

- Instala un crate binario:

`cargo install {{nombre_crate}}`

- Lista los crates binarios instalados:

`cargo install --list`

- Crea un nuevo proyecto Rust binario o de biblioteca en el directorio especificado (o en el directorio de trabajo actual por defecto):

`cargo init --{{bin|lib}} {{ruta/al/directorio}}`

- Añade una dependencia a `Cargo.toml` en el directorio actual:

`cargo add {{dependencia}}`

- Construye el proyecto Rust en el directorio actual utilizando el perfil de lanzamiento:

`cargo build --release`

- Construye el proyecto Rust en el directorio actual utilizando el compilador nightly (requiere `rustup`):

`cargo +nightly build`

- Construye usando un número específico de hilos (por defecto es el número de CPUs lógicas):

`cargo build --jobs {{numero_de_hilos}}`
