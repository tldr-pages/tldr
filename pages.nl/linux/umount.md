# umount

> Koppel een bestandssysteem los vanuit het mount-punt, waardoor het niet langer toegankelijk is.
> Een bestandssysteem kan niet losgekoppeld worden als het bezig is.
> Meer informatie: <https://manned.org/umount.8>.

- Koppel een bestandssysteem los door het pad op te geven van de bron waarop het gemount is:

`sudo umount {{pad/naar/apparaat_bestand}}`

- Koppel een bestandssysteem los door het pad op te geven waarop het gemount is:

`sudo umount {{pad/naar/gemounte_map}}`

- Als het loskoppelen faalt, probeer het bestandssysteem dan opnieuw te koppelen in leesmodus:

`sudo umount {{[-r|--read-only]}} {{pad/naar/gemounte_map}}`

- Koppel ieder gespecificeerde map recursief los:

`sudo umount {{[-R|--recursive]}} {{pad/naar/gemounte_map}}`

- Koppel alle gemounte bestandssystemen los (behalve het `proc` bestandssysteem):

`sudo umount {{[-a|--all]}}`
