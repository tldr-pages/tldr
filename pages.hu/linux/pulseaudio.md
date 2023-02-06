# pulseaudio

> A PulseAudio hangrendszer démon és menedzser. További információ: <https://www.freedesktop.org/wiki/Software/PulseAudio/>.

- Ellenőrizze, hogy a PulseAudio fut-e (a nem nulla kilépési kód azt jelenti, hogy nem fut):

`pulseaudio --check`

- Indítsa el a PulseAudio démont a háttérben:

`pulseaudio --start`

- A futó PulseAudio daemon leállítása:

`pulseaudio --kill`

- A rendelkezésre álló modulok listája:

`pulseaudio --dump-modules`

- A modul betöltése az éppen futó démonba a megadott argumentumokkal:

`pulseaudio --load="{{module_name}} {{arguments}}"`
