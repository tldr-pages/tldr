# sk

> Fuzzy finder geschreven in Rust.
> Zie ook: `fzf`.
> Meer informatie: <https://github.com/skim-rs/skim>.

- Start `skim` op alle bestanden in de opgegeven map:

`find {{pad/naar/map}} -type f | sk`

- Start `skim` voor actieve processen:

`ps aux | sk`

- Start `skim` met een bepaalde query:

`sk --query "{{query}}"`

- Selecteer meerdere bestanden met `<Shift Tab>` en schrijf naar een bestand:

`find {{pad/naar/map}} -type f | sk --multi >{{pad/naar/bestand}}`
