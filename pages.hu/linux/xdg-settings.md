# xdg-settings

> Az XDG-kompatibilis asztali környezetek beállításainak kezelése. További információ: <https://portland.freedesktop.org/doc/xdg-settings.html>.

- Az alapértelmezett webböngésző nyomtatása:

`xdg-settings get {{default-web-browser}}`

- Az alapértelmezett webböngésző beállítása Firefox-ra:

`xdg-settings set {{default-web-browser}} {{firefox.desktop}}`

- Állítsa be az alapértelmezett levelezési URL-séma kezelőjét Evolutionra:

`xdg-settings set {{default-url-scheme-handler}} {{mailto}} {{evolution.desktop}}`

- Állítsa be az alapértelmezett PDF-dokumentumnézegetőt:

`xdg-settings set {{pdf-viewer.desktop}}`

- Súgó megjelenítése:

`xdg-settings --help`
