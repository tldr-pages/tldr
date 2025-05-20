# nix

> Un potente gestor de paquetes que hace la gestión de paquetes fiable, reproducible y declarativa.
> `nix` es experimental y requiere permitir funcionalidades experimentales. Para una interfaz clásica y estable, vea también `tldr nix classic`.
> Algunos subcomandos como `build`, `develop`, `flake`, `registry`, `profile`, `search`, `repl`, `store`, `edit`, `why-depends`, etc. tienen sus propias páginas.
> Más información: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix>.

- Habilita el comando `nix`:

`mkdir {{[-p|--parents]}} ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- Busca un paquete en nixpkgs usando su nombre o descripción:

`nix search nixpkgs {{término_de_búsqueda}}`

- Inicia un shell con unos paquetes de nixpkgs disponibles:

`nix shell {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Instala unos paquetes de nixpkgs de manera permanente:

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- Quita rutas desusadas del almacén de Nix para liberar espacio:

`nix store gc`

- Inicia un entorno interactivo para evaluar expresiones de Nix:

`nix repl`

- Muestra ayuda para cada subcomando específico:

`nix help {{subcomando}}`
