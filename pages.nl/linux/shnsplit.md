# shnsplit

> Splitst audiobestanden volgens een `.cue` bestand.
> Meer informatie: <http://shnutils.freeshell.org/shntool/>.

- Splits een `.wav` + `.cue` bestand in meerdere bestanden:

`shnsplit -f {{pad/naar/bestand.cue}} {{pad/naar/bestand.wav}}`

- Toon ondersteunde formaten:

`shnsplit -a`

- Splits een `.flac` bestand in meerdere bestanden:

`shnsplit -f {{pad/naar/bestand.cue}} -o flac {{pad/naar/bestand.flac}}`

- Splits een `.wav` bestand in meerdere bestanden in de vorm van "track-nummer - album - titel":

`shnsplit -f {{pad/naar/bestand.cue}} {{pad/naar/bestand.wav}} -t "%n - %a - %t`
