# flatpak run

> Ejecuta aplicaciones y tiempos de ejecución flatpak.
> Más información: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- Ejecuta una aplicación instalada:

`flatpak run {{com.example.app}}`

- Ejecuta una aplicación instalada desde una rama específica, por ejemplo, stable, beta, master:

`flatpak run --branch={{stable|beta|master|...}} {{com.example.app}}`

- Ejecuta un shell interactivo dentro de un flatpak:

`flatpak run --command={{sh}} {{com.example.app}}`
