# Chezmoi

> Un manager de dotfile multi-mașină, scris în Go.
> Mai multe informaţii: <https://chezmoi.io>

- Inițializarea chezmoi pe mașină:

`chezmoi init`

- Spune-i chezmoi pentru a gestiona un dotfile:

`chezmoi add {{path/to/file}}`

- Editați starea sursă a unui dotfile urmărite:

`chezmoi edit {{path/to/file}}`

- A se vedea modificările chezmoi ar face:

`chezmoi diff`

- Aplicați modificările:

`chezmoi -v apply`

- Setați chezmoi pe o altă mașină prin descărcarea dotfiles existente dintr-un depozit Git:

`chezmoi init {{https://example.com/path/to/repository.git}}`

- Adu cele mai recente modificări dintr-un depozit la distanță:

`chezmoi update`
