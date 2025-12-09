# nix-collect-garbage

> Elimina rutas del almacén de nix desusados o inalcanzables.
> Las generaciones se pueden listar usando `nix-env --list-generations`.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>.

- Elimina todas las rutas del almacén desusados por las generaciones actuales de cada perfil:

`nix-collect-garbage {{[-d|--delete-old]}}`

- Simula la eliminación de rutas del almacén antiguas:

`nix-collect-garbage {{[-d|--delete-old]}} --dry-run`

- Elimina todas las rutas del almacén más antiguas que 30 días:

`nix-collect-garbage --delete-older-than 30d`
