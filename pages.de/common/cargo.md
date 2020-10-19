# cargo

> Rust Paketmanager.
> Verwalte Rust-Projekte und deren Abhängigkeiten (crates).
> Mehr Informationen: <https://crates.io/>.

- Suche nach Abhängigkeiten (crates):

`cargo search {{suchwort}}`

- Installiere eine Abhängigkeit (crate):

`cargo install {{abhängigkeits_name}}`

- Liste alle installierten Abhängigkeiten (crates) auf:

`cargo install --list`

- Erzeuge eine neues Rust-Projekt als Anwendung oder Bibliothek im aktuellen Verzeichnis:

`cargo init --{{bin|lib}}`

- Erzeuge eine neues Rust-Projekt als Anwendung oder Bibliothek im angegebenen Verzeichnis:

`cargo new {{pfad/zum/verzeichnis}} --{{bin|lib}}`

- Erstelle (bzw. kompiliere) das Rust-Projekt im aktuellen Verzeichnis:

`cargo build`

- Erstelle (bzw. kompiliere) mit einer bestimmten Anzahl an Threads (Standard ist die Anzahl der CPU-Kerne):

`cargo build -j {{jobs}}`
