# amixer

> Mixer für den ALSA Soundkarten Treiber.
> Mehr Informationen: <https://manned.org/amixer>.

- Erhöhe die Haupt Lautstärke um 10%:

`amixer -D pulse sset Master {{10%+}}`

- Verringere die Haupt Lautstärke um 10%:

`amixer -D pulse sset Master {{10%-}}
