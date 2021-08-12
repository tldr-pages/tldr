# cargo

> Managerul de pachete Rust.
> Gestionați proiectele Rust și dependențele modulelor acestora (lăzi).
> Mai multe informaţii: <https://crates.io/>

- Caută lăzi:

`cargo search {{search_string}}`

- Instalați o ladă:

`cargo install {{crate_name}}`

- Lista de lăzi instalate:

`cargo install --list`

- Creați un nou proiect binar sau bibliotecă Rust în directorul curent:

`cargo init --{{bin|lib}}`

- Creați un nou proiect binar sau bibliotecă Rust în directorul specificat:

`cargo new {{path/to/directory}} --{{bin|lib}}`

- Construiți proiectul Rust în directorul curent:

`cargo build`

- Construiți folosind un anumit număr de fire (implicit este numărul de nuclee CPU):

`cargo build -j {{jobs}}`
