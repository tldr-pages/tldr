# nix

> Utilitare pentru limba și magazinul Nix.
> Mai multe informaţii: <https://nixos.org>

- Căutați un pachet prin numele sau descrierea acestuia:

`nix search {{search_term}}`

- Începeți o coajă Nix cu pachetele specificate disponibile:

`nix run {{nixpkgs.pkg1 nixpkgs.pkg2 nixpkgs.pkg3...}}`

- Optimizați utilizarea discului magazin Nix prin combinarea fișierelor duplicate:

`nix optimise-store`

- Începeți un mediu interactiv pentru evaluarea expresiilor Nix:

`nix repl`

- Upgrade Nix la cea mai recentă versiune stabilă:

`nix upgrade-nix`
