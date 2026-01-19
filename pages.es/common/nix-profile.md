# nix profile

> Instala, actualiza y elimina paquetes de los perfiles Nix.
> Más información: <https://nix.dev/manual/nix/latest/command-ref/new-cli/nix3-profile.html>.

- Instala paquetes de nixpkgs en el perfil predeterminado:

`nix profile add {{nixpkgs#pkg1 nixpkgs#pkg2 ...}}`

- Instala un paquete de un flake en GitHub en un perfil personalizado:

`nix profile add {{github:owner/repo/pkg}} --profile {{ruta/al/directorio}}`

- Enumera los paquetes actualmente instalados en el perfil predeterminado:

`nix profile list`

- Elimina un paquete instalado desde nixpkgs del perfil predeterminado, por nombre:

`nix profile remove {{legacyPackages.x86_64-linux.pkg}}`

- Actualiza los paquetes del perfil predeterminado a las últimas versiones disponibles:

`nix profile upgrade --all`

- Revierte (cancela) la última acción en el perfil predeterminado:

`nix profile rollback`

Traducción realizada con la versión gratuita del traductor DeepL.com
