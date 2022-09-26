# beep

> Ein Befehl, um den PC-Lautsprecher zu steuern.
> Weitere Informationen: <https://github.com/spkr-beep/beep>.

- Gib einen Ton aus:

`beep`

- Gib einen Ton mehrmals aus:

`beep -r {{wiederholungen}}`

- Gib einen Ton mit einer bestimmten Frequenz (Hz) und Länge (Millisekunden) aus:

`beep -f {{frequenz}} -l {{länge}}`

- Spiele jede neue Frequenz und Länge als einen eigenen Ton:

`beep -f {{frequenz}} -l {{länge}} -n -f {{frequenz}} -l {{länge}}`

- Spiele die C-Dur-Tonleiter:

`beep -f {{262}} -n -f {{294}} -n -f {{330}} -n -f {{349}} -n -f {{392}} -n -f {{440}} -n -f {{494}} -n -f {{523}}`
