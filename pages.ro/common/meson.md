# meson

> Scons-like sistem de compilare care utilizează Python ca limbă front-end și Ninja ca backend de construcție.
> Mai multe informaţii: <https://mesonbuild.com>

- Generează un proiect c cu un nume și o versiune dată:

`meson init --language={{c}} --name={{myproject}} --version={{0.1}}`

- Configurarea `builddir` cu valori implicite:

`meson setup {{build_dir}}`

- Construirea proiectului:

`meson compile -C {{path/to/build_dir}}`

- Arată ajutorul:

`meson --help`

- Arată informaţii despre versiune:

`meson --version`
