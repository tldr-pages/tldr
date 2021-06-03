# flatpak-builder

> Help build application dependencies.
> More information: <https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>.

- Build a Flatpak, then export it to a new repository:

`flatpak-builder {{path/to/build_dir}} {{path/to/manifest}}`

- Build a Flatpak, then export it to the specified repository:

`flatpak-builder --repo={{repo}} {{path/to/build_dir}} {{path/to/manifest}}`

- Build a Flatpak, then install it locally:

`flatpak-builder --install {{path/to/build_dir}} {{path/to/manifest}}`

- Build and sign a Flatpak, then export it to the specified repository:

`flatpak-builder --gpg-sign={{key_id}} --repo={{repository}} {{path/to/manifest}}`

- Run a shell inside of an applications sandbox without installing it:

`flatpak-builder --run {{path/to/build_dir}} {{path/to/manifest}} sh`
