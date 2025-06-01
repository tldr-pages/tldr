# nix store

> Manipula el almacén de Nix.
> Vea también: `nix-store`.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-store.html>.

- Recolecta basura, es decir, elimina rutas desusadas para reducir el uso de disco:

`nix store gc`

- Crea un enlace físico entre archivos idénticos para reducir el uso de disco:

`nix store optimise`

- Elimina una ruta específica en el almacén (debe ser desusada):

`nix store delete {{/nix/store/...}}`

- Lista el contenido de una ruta en el almacén, en un almacén remoto:

`nix store --store {{https://cache.nixos.org}} ls {{/nix/store/...}}`

- Muestra las diferencias de versiones entre dos rutas del almacén, con sus dependencias respectivas:

`nix store diff-closures {{/nix/store/...}} {{/nix/store/...}}`
