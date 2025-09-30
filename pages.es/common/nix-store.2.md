# nix-store

> Manipula o busca en el almacén de Nix.
> Vea también: `nix store.3`.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/nix-store.html>.

- Recolecta basura, por ejemplo quitar las rutas desusadas:

`nix-store --gc`

- Crea un enlace físico entre archivos idénticos para reducir el uso de disco:

`nix-store --optimise`

- Elimina una ruta específica en el almacén (debe ser desusada):

`nix-store --delete {{/nix/store/...}}`

- Muestra todas las dependencias de una ruta del almacén (paquete), en un formato de árbol:

`nix-store {{[-q|--query]}} --tree {{/nix/store/...}}`

- Calcula el tamaño total de una ruta específica del almacén con todas las dependencias:

`du {{[-cLsh|--total --dereference --summarize --human-readable]}} $(nix-store {{[-q|--query]}} --references {{/nix/store/...}})`

- Muestra todos los dependientes de una ruta particular del almacén:

`nix-store {{[-q|--query]}} --referrers {{/nix/store/...}}`
