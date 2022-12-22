# nix-collect-garbage

> Löschen von unbenutzten und unerreichbaren Nix-Speicherpfaden.
> Generationen können mit `nix-env --list-generations` aufgelistet werden.
> Weitere Informationen: <https://nixos.org/releases/nix/latest/manual/#sec-nix-collect-garbage>.

- Löschen von allen Speicherpfaden, die von den aktuellen Generationen der einzelnen Profile nicht verwendet werden:

`sudo nix-collect-garbage --delete-old`

- Simulieren der Löschung alter Speicherpfade:

`sudo nix-collect-garbage --delete-old --dry-run`

- Löschen aller Speicherpfade, die älter als 30 Tage sind:

`sudo nix-collect-garbage --delete-older-than 30d`
