# nixos-option

> Inspecciona una configuración de NixOS.
> Más información: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- Lista todas las subclaves de una clave de opciones proporcionadas:

`nixos-option {{clave}}`

- Lista los módulos de arranque del kernel actuales:

`nixos-option boot.kernelModules`

- Lista claves autorizadas para un usuario específico:

`nixos-option users.users.{{nombre_del_usuario}}.openssh.authorizedKeys.{{archivoDeClaves|clave}}`

- Lista todos los constructores remotos:

`nixos-option nix.buildMachines`

- Lista todas las subclaves de una clave proporcionada en otra configuración de NixOS:

`NIXOS_CONFIG={{ruta_a_configuracion.nix}} nixos-option {{clave}}`

- Muestra recursivamente todos los valores de un usuario:

`nixos-option {{[-r|--recursive]}} users.users.{{usuario}}`
