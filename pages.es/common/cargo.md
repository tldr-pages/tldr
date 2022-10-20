# cargo

> Gestiona proyectos Rust y sus dependencias de módulos (crates).
> Algunos subcomandos como `cargo build` tienen su propia documentación de uso.
> Más información: <https://crates.io>.

- Busca crates:

`cargo search {{texto_de_búsqueda}}`

- Instala un crate:

`cargo install {{nombre_del_módulo}}`

- Lista crates instalados:

`cargo install --list`

- Crea un nuevo proyecto Rust binario o biblioteca en el directorio actual:

`cargo init --{{bin|lib}}`

- Crea un nuevo proyecto Rust binario o biblioteca en el directorio especificado:

`cargo new {{path/to/directory}} --{{bin|lib}}`

- Compila el proyecto de Rust en el directorio actual:

`cargo build`

- Compila el proyecto de Rust en el directorio actual usando el compilador __nightly__:

`cargo +nightly build`

- Compila el proyecto de Rust en el directorio actual usando un número específico de hilos (por defecto es el número de núcleos del CPU):

`cargo build --jobs {{number_of_threads}}`
