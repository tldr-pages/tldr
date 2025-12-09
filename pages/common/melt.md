# melt

> Backup and restore Ed25519 SSH keys using memorizable seed phrases.
> More information: <https://github.com/charmbracelet/melt#usage>.

- Generate a seed phrase from an existing Ed25519 private key:

`melt {{~/.ssh/id_ed25519}}`

- Generate a seed phrase from `stdin`:

`{{cat ~/.ssh/id_ed25519}} | melt`

- Restore an SSH key from a seed phrase:

`melt restore {{path/to/key}} --seed "{{seed_phrase}}"`

- Restore an SSH key from a seed phrase via `stdin`:

`{{cat path/to/file}} | melt restore -`
