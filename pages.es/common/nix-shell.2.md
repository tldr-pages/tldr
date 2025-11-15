# nix-shell

> Inicia un shell interactivo basado on una expresión de Nix.
> Vea también: `nix shell.3`.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/nix-shell.html>.

- Inicia con una expresión de nix en `shell.nix` o `default.nix` del directorio actual:

`nix-shell`

- Ejecuta un comando de shell en un shell no interactivo y sale:

`nix-shell --run "{{comando}} {{argumento1 argumento2 ...}}"`

- Ejecuta con la expresión en `default.nix` en el directorio actual:

`nix-shell {{default.nix}}`

- Inicia con paquetes cargados de nixpkgs:

`nix-shell {{[-p|--packages]}} {{paquete1 paquete2 ...}}`

- Inicia con paquetes cargados desde una revisión específica de nixpkgs:

`nix-shell {{[-p|--packages]}} {{paquete1 paquete2 ...}} {{[-I|--include]}} nixpkgs={{https://github.com/NixOS/nixpkgs/archive/revision_de_nixpkgs.tar.gz}}`

- Evalua el resto de un archivo en un interpretador, para usarse con `#!-scripts` (vea también <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>):

`nix-shell -i {{interpretador}} {{[-p|--packages]}} {{paquete1 paquete2 ...}}`
