# nix run

> Ejecuta una aplicación desde un flake de Nix.
> Vea también: `nix flake` para información sobre los flakes.
> Más información: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-run.html>.

- Ejecuta la aplicación predeterminada del flake en el directorio actual:

`nix run`

- Ejecuta un comando cuyo nombre iguala el nombre de un paquete de nixpkgs (si quieres un comando diferente de ese paquete, ver también `tldr nix shell`):

`nix run nixpkgs#{{pkg}}`

- Ejecuta un comando con los argumentos proporcionados:

`nix run nixpkgs#{{vim}} -- {{ruta/al/archivo}}`

- Ejecuta desde un repositorio remoto:

`nix run {{nombre_de_remoto}}:{{dueño}}/{{repositorio}}`

- Ejecuta desde un repositorio remoto usando una etiqueta específica, revisión o rama:

`nix run {{nombre_de_remoto}}:{{dueño}}/{{repositorio}}/{{referencia}}`

- Ejecuta desde un repositorio remoto especificando un subdirectorio y un programa:

`nix run "{{nombre_de_remoto}}:{{dueño}}/{{repositorio}}?dir={{nombre_del_directorio}}#{{aplicación}}"`

- Ejecuta el flake de una solicitud de incorporación de cambios de GitHub:

`nix run github:{{dueño}}/{{repositorio}}/pull/{{número}}/head`
