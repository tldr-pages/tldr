# amixer

> Mixer az ALSA hangkártya vezérlőhöz. További információ: <https://manned.org/amixer>.

- Növelje a főhangerőt 10%-kal:

`amixer -D pulse sset Master {{10%+}}`

- Csökkentse a master hangerőt 10%-kal:

`amixer -D pulse sset Master {{10%-}}`
