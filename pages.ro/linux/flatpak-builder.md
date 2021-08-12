# flatpak-builder

> Ajutați la construirea dependențelor de aplicații.
> Mai multe informaţii: <https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>

- Construiți un Flatpak și exportați-l într-un nou depozit:

`flatpak-builder {{path/to/build_directory}} {{path/to/manifest}}`

- Construiți un Flatpak și exportați-l în depozitul specificat:

`flatpak-builder --repo={{repository_name}} {{path/to/build_directory}} {{path/to/manifest}}`

- Construiți un Flatpak și instalați-l la nivel local:

`flatpak-builder --install {{path/to/build_directory}} {{path/to/manifest}}`

- Construiți și semnați un Flatpak și exportați-l în depozitul specificat:

`flatpak-builder --gpg-sign={{key_id}} --repo={{repository_name}} {{path/to/manifest}}`

- Rulați o coajă în interiorul unei cutii de nisip de aplicație fără a o instala:

`flatpak-builder --run {{path/to/build_directory}} {{path/to/manifest}} {{sh}}`
