# cargo

> Verwalte Rust-Projekte und deren Abhängigkeiten (crates).
> Manche Unterbefehle wie `cargo build` sind separat dokumentiert.
> Weitere Informationen: <https://doc.rust-lang.org/cargo>.

- Suche nach Abhängigkeiten (crates):

`cargo search {{suche}}`

- Installiere eine Abhängigkeit (crate):

`cargo install {{abhängigkeit}}`

- Liste alle installierten Abhängigkeiten (crates) auf:

`cargo install --list`

- Erzeuge ein neues Rust-Projekt als Anwendung oder Bibliothek im aktuellen Verzeichnis:

`cargo init --{{bin|lib}}`

- Erzeuge ein neues Rust-Projekt als Anwendung oder Bibliothek im angegebenen Verzeichnis:

`cargo new {{pfad/zu/verzeichnis}} --{{bin|lib}}`

- Erstelle (bzw. kompiliere) ein Rust-Projekt im aktuellen Verzeichnis:

`cargo build`

- Erstelle (bzw. kompiliere) ein Rust-Projekt mit einer bestimmten Anzahl an Threads (standardmäßig die Anzahl der CPU-Kerne):

`cargo build --jobs {{thread_anzahl}}`
