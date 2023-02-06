# meson

> SCons-szerű build rendszer, amely pythont használ front-end nyelvként és Ninja-t backendként. További információ: <https://mesonbuild.com>.

- Generál egy C projektet adott névvel és verzióval:

`meson init --language={{c}} --name={{myproject}} --version={{0.1}}`

- A `builddir` alapértelmezett értékekkel történő beállítása:

`meson setup {{build_dir}}`

- Építse a projektet:

`meson compile -C {{path/to/build_dir}}`

- A projektben lévő összes teszt futtatása:

`meson test`

- A súgó megjelenítése:

`meson --help`

- Verzióinformáció megjelenítése:

`meson --version`
