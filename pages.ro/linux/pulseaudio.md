# pulseaudio

> Daemon sistem de sunet pulseaudio și manager.
> Mai multe informaţii: <https://www.freedesktop.org/wiki/Software/PulseAudio/>

- Verificați dacă pulseaudio rulează (un cod de ieșire non-zero înseamnă că nu rulează):

`pulseaudio --check`

- Porniți daemonul pulseaudio în fundal:

`pulseaudio --start`

- Omoară daemonul pulseaudio care rulează:

`pulseaudio --kill`

- Lista modulelor disponibile:

`pulseaudio --dump-modules`

- Încărcați un modul în daemonul care rulează în prezent cu argumentele specificate:

`pulseaudio --load="{{module_name}} {{arguments}}"`
