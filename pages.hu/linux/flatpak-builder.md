# flatpak-builder

> Segít az alkalmazásfüggőségek kialakításában. További információ: <https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>.

- Építsen egy Flatpakot, és exportálja egy új tárolóhelyre:

`flatpak-builder {{path/to/build_directory}} {{path/to/manifest}}`

- Flatpakot készít és exportálja a megadott tárolóhelyre:

`flatpak-builder --repo={{repository_name}} {{path/to/build_directory}} {{path/to/manifest}}`

- Flatpak készítése és helyi telepítése:

`flatpak-builder --install {{path/to/build_directory}} {{path/to/manifest}}`

- Flatpak készítése és aláírása, majd exportálása a megadott tárolóhelyre:

`flatpak-builder --gpg-sign={{key_id}} --repo={{repository_name}} {{path/to/manifest}}`

- Shell futtatása egy alkalmazás homokozójában telepítés nélkül:

`flatpak-builder --run {{path/to/build_directory}} {{path/to/manifest}} {{sh}}`
