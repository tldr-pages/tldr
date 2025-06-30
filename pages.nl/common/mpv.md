# mpv

> Een audio-/videospeler gebaseerd op MPlayer.
> Zie ook: `mplayer`, `vlc`.
> Meer informatie: <https://mpv.io/manual/stable/>.

- Speel een video of audio af van een URL of bestand:

`mpv {{url|pad/naar/bestand}}`

- Spring 5 seconden vooruit/achteruit:

`{{<ArrowLeft>|<ArrowRight>}}`

- Spring een minuut vooruit/achteruit:

`{{<ArrowDown>|<ArrowUp>}}`

- Verlaag of verhoog de afspeelsnelheid met 10%:

`{{<[>|<]>}}`

- Voeg ondertiteling toe vanuit een bestand:

`mpv --sub-file={{pad/naar/bestand}}`

- Maak een screenshot van het huidige frame (standaard opgeslagen als `./mpv-shotNNNN.jpg`):

`<s>`

- Speel een bestand af op een opgegeven snelheid (standaard 1):

`mpv --speed {{0.01..100}} {{pad/naar/bestand}}`

- Speel een bestand af met een profiel gedefinieerd in het `mpv.conf` bestand:

`mpv --profile {{profiel_naam}} {{pad/naar/bestand}}`
