# nix-collect-garbage

> Ștergeți căile de stocare nix neutilizate și inaccesibile.
> Generațiile pot fi listate folosind `nix-env —list-generations`.
> Mai multe informaţii: <https://nixos.org/releases/nix/latest/manual/#sec-nix-collect-garbage>

- Ștergeți toate căile magazinului neutilizate de generațiile curente ale fiecărui profil:

`sudo nix-collect-garbage --delete-old`

- Simulați ștergerea vechilor căi de magazin:

`sudo nix-collect-garbage --delete-old --dry-run`

- Ștergeți toate căile magazinului mai vechi de 30 de zile:

`sudo nix-collect-garbage --delete-older-than {{30d}}`
