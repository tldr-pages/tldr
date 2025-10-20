# melt

> Backup and restore Ed25519 SSH keys using memorizable seed phrases.
> More information: <https://github.com/charmbracelet/melt>.

- Generate a seed phrase from an existing Ed25519 private key:
`melt {{~/.ssh/id_ed25519}}`

- Generate a seed phrase from standard input:
`cat {{~/.ssh/id_ed25519}} | melt`

- Restore an SSH key from a seed phrase:
`melt restore {{./my-key}} --seed "{{seed phrase}}"`

- Restore an SSH key from a seed phrase via standard input:
`cat {{words}} | melt restore -`
