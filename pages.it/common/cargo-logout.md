# cargo logout

> Rimuovi un token API del registro localmente.
> Il token viene usato per autenticarsi verso un registro di pacchetti. Puoi aggiungerlo nuovamente con `cargo login`.
> Maggiori informazioni: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- Rimuovi un token API dallo storage delle credenziali locali (situato in `$CARGO_HOME/credentials.toml`):

`cargo logout`

- Usa il registro specificato (i nomi dei registri possono essere definiti nella configurazione - il predefinito è <https://crates.io>):

`cargo logout --registry {{nome}}`
