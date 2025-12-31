# stow

> Symlink-beheerder.
> Vaak gebruikt om dotfiles te beheren.
> Zie ook: `chezmoi`, `tuckr`, `vcsh`, `homeshick`.
> Meer informatie: <https://www.gnu.org/software/stow/manual/stow.html#Invoking-Stow>.

- Symlink alle bestanden recursief naar de opgegeven map:

`stow {{[-t|--target]}} {{pad/naar/doel_map}} {{bestand1 map1 bestand2 map2}}`

- Verwijder alle symlinks recursief in de opgegeven map:

`stow {{[-D|--delete]}} {{[-t|--target]}} {{pad/naar/doel_map}} {{bestand1 map1 bestand2 map2}}`

- Simuleer om te zien hoe het resultaat eruit ziet:

`stow {{[-n|--simulate]}} {{[-t|--target]}} {{pad/naar/doel_map}} {{bestand1 map1 bestand2 map2}}`

- Verwijder en maak opnieuw de symlinks aan:

`stow {{[-R|--restow]}} {{[-t|--target]}} {{pad/naar/doel_map}} {{bestand1 map1 bestand2 map2}}`

- Sluit bestanden uit die overeenkomen met een reguliere expressie:

`stow --ignore={{reguliere_expressie}} {{[-t|--target]}} {{pad/naar/doel_map}} {{bestand1 map1 bestand2 map2}}`
