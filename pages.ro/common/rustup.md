# rustup

> Rust instrument de instalare a lanțului de instrumente.
> Instalați, gestionați și actualizați lanțurile de instrumente Rust.
> Mai multe informaţii: <https://github.com/rust-lang/rustup.rs>

- Instalați lanțul de instrumente de noapte pentru sistemul dvs.:

`rustup install nightly`

- Comutați lanțul de instrumente implicit pe timp de noapte, astfel încât comenzile `încărcătură și `rugin` să o folosească:

`rustup default nightly`

- Utilizați lanțul de instrumente de noapte în interiorul proiectului curent, dar lăsați setările globale neschimbate:

`rustup override set nightly`

- Actualizează toate lanţurile de instrumente:

`rustup update`

- Lista de instrumente instalate:

`rustup show`

- Rulați construirea de marfă cu un anumit lanț de instrumente:

`rustup run {{toolchain_name}} cargo build`

- Deschideți documentația locală de rugină în browserul web implicit:

`rustup doc`
