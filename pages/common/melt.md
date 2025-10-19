# melt

> Backup and restore Ed25519 SSH keys using memorizable seed phrases.
> More information: <https://github.com/charmbracelet/melt>.

- Generate a seed phrase from an existing SSH key:

`melt {{~/.ssh/id_ed25519}}`

- Generate a seed phrase from standard input:

`cat {{~/.ssh/id_ed25519}} | melt`

- Restore an SSH key from a seed phrase:

`melt restore {{./my-key}} --seed "{{seed phrase}}"`

- Rebuild an SSH key from a seed phrase and print it to standard output:

`cat {{words}} | melt restore -`