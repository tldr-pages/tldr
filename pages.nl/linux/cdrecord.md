# cdrecord

> Schrijf gegevens naar cd's of dvd's.
> Sommige aanroepen van cdrecord kunnen destructieve acties veroorzaken, zoals het wissen van alle gegevens op een schijf.
> Meer informatie: <https://manned.org/cdrecord>.

- Toon optische stations die beschikbaar zijn voor `cdrecord`:

`cdrecord --devices`

- Neem een audio-only schijf op ("branden"):

`cdrecord dev={{/dev/optisch_station}} -audio {{track*.cdaudio}}`

- Brand een bestand naar een schijf en werp de schijf uit zodra dit klaar is (sommige recorders vereisen dit):

`cdrecord -eject dev={{/dev/optisch_station}} -data {{bestand.iso}}`

- Brand een bestand naar de schijf in een optisch station, mogelijk naar meerdere schijven achter elkaar:

`cdrecord -tao dev={{/dev/optisch_station}} -data {{bestand.iso}}`
