# amixer

> Mixer für den ALSA Soundkarten-Treiber.
> Weitere Informationen: <https://manned.org/amixer>.

- Erhöhe den Gesamtpegel um 10%:

`amixer -D pulse sset Master {{10%+}}`

- Verringere den Gesamtpegel um 10%:

`amixer -D pulse sset Master {{10%-}}`
