# cargo install

> Compila e installa un binario Rust.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-install.html>.

- Installa un pacchetto da <https://crates.io> (la versione è opzionale - di default l'ultima):

`cargo install {{pacchetto}}@{{versione}}`

- Installa un pacchetto dal repository Git specificato:

`cargo install --git {{repo_url}}`

- Compila dal branch/tag/commit specificato quando si installa da un repository Git:

`cargo install --git {{repo_url}} --{{branch|tag|rev}} {{branch_name|tag|commit_hash}}`

- Installa un pacchetto da una directory locale:

`cargo install --path {{percorso/del/package}}`

- Elenca tutti i pacchetti installati e le loro versioni:

`cargo install --list`
