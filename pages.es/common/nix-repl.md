# nix repl

> Inicia un entorno interactivo para evaluar expresiones de Nix.
> Vea <https://nixos.org/manual/nix/stable/language/index.html> para una descripción del lenguaje de expresiones de Nix.
> Más información: <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-repl.html>.

- Inicia un entorno interactivo para evaluar expresiones de Nix:

`nix repl`

- [Interactivo] Carga todos los paquetes desde un flake (ej. `nixpkgs`) al ámbito:

`:lf {{nixpkgs}}`

- [Interactivo] Construye un paquete desde una expresión:

`:b {{expresión}}`

- [Interactivo] Inicia un shell con un paquete de la expresión disponible:

`:u {{expresión}}`

- [Interactivo] Inicia un shell con las dependencias del paquete de la expresión disponible:

`:s {{expresión}}`
