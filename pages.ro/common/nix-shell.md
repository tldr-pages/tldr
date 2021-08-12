# nix-shell

> Porniți o coajă interactivă bazată pe o expresie Nix.
> Mai multe informaţii: <https://nixos.org/manual/nix/stable/#sec-nix-shell>

- Începeți cu expresia nix în `shell.nix` sau `default.nix` în directorul curent:

`nix-shell`

- Executați comanda shell în coajă non-interactivă și ieșire:

`nix-shell --run "{{command}} {{command_arguments}}"`

- Începeți cu expresia în `default.nix` în directorul curent:

`nix-shell {{default.nix}}`

- Începeți cu pachetele încărcate de la nixpkgs:

`nix-shell --packages {{package_name_1}} {{package_name_2}}`

- Începeți cu pachetele încărcate de la revizuirea nixpkgs specifice:

`nix-shell --packages {{package_names}} -I nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz}}`

- Evaluați restul fișierului în interpret specific, pentru utilizare în `#! -scripturi „(a se vedea  <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i {{interpreter}} --packages {{package_names}}`
