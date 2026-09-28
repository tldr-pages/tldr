# tuckr

> Dotfile-beheerder geschreven in Rust.
> Zie ook: `chezmoi`, `vcsh`, `homeshick`, `stow`.
> Meer informatie: <https://github.com/RaphGL/Tuckr#usage>.

- Controleer de dotfile-status:

`tuckr status`

- Voeg alle dotfiles toe aan het systeem:

`tuckr add \*`

- Voeg alle dotfiles toe, behalve de opgegeven programma's:

`tuckr add \* -e {{programma1}},{{programma2}}`

- Verwijder alle dotfiles van het systeem:

`tuckr rm \*`

- Voeg een programma-dotfile toe en voer het bijbehorende setup-script uit:

`tuckr set {{programma}}`
