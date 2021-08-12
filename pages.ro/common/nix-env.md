# nix-env

> Manipularea sau interogarea mediilor de utilizator Nix.
> Mai multe informaţii: <https://nixos.org/manual/nix/stable/#sec-nix-env>

- Listează toate pachetele instalate:

`nix-env -q`

- Interogare pachete instalate:

`nix-env -q {{search_term}}`

- Interogare pachete disponibile:

`nix-env -qa {{search_term}}`

- Pachet de instalare:

`nix-env -iA nixpkgs.{{pkg_name}}`

- Instalați un pachet dintr-un URL:

`nix-env -i {{pkg_name}} --file {{example.com}}`

- Pachet de dezinstalare:

`nix-env -e {{pkg_name}}`

- Upgrade un pachet:

`nix-env -u {{pkg_name}}`

- Upgrade toate pachetele:

`nix-env -u`
