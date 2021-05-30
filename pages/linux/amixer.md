# amixer

> Mixer for ALSA soundcard driver.
> More information: <https://wiki.archlinux.org/title/Advanced_Linux_Sound_Architecture>.

- Turn up the master volume by 10%:

`amixer -D pulse sset Master {{10%+}}`

- Turn down the master volume by 10%:

`amixer -D pulse sset Master {{10%-}}`
