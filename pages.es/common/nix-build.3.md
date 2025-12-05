# nix build

> Construye una expresión de Nix (descargando desde caché cuando sea posible).
> Vea también: `nix-build` para información sobre construcciones tradicionales de Nix desde expresiones, `nix flake` para información sobre los flakes.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-build.html>.

- Construye un paquete desde nixpkgs, creando un enlace simbólico al resultado en `./result`:

`nix build {{nixpkgs#pkg}}`

- Construye un paquete desde un flake en el directorio actual, mostrando el registro de construcción en el proceso:

`nix build {{[-L|--print-build-logs]}} {{.#pkg}}`

- Construye el paquete predeterminado de un flake en algún directorio:

`nix build {{./ruta/al/directorio}}`

- Construye un paquete sin hacer el enlace simbólico `result`, mostrando a su vez la ruta del almacén de Nix en `stdout`:

`nix build --no-link --print-out-paths`
