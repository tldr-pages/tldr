# beep

> Ein Befehl, um den PC-Lautsprecher zu steuern.
> Weitere Informationen: <https://manned.org/man/beep>.

- Gib einen Ton aus:

`beep`

- Gib einen Ton mehrmals aus:

`beep -r {{wiederholungen}}`

- Gib einen Ton mit einer bestimmten Frequenz (Hz) und Länge (Millisekunden) aus:

`beep -f {{frequenz}} -l {{länge}}`

- Spiele jede neue Frequenz und Länge als einen eigenen Ton:

`beep -f {{frequenz}} -l {{länge}} {{[-n|--new]}} -f {{frequenz}} -l {{länge}}`

- Spiele die C-Dur-Tonleiter:

`beep -f {{262}} {{[-n|--new]}} -f {{294}} {{[-n|--new]}} -f {{330}} {{[-n|--new]}} -f {{349}} {{[-n|--new]}} -f {{392}} {{[-n|--new]}} -f {{440}} {{[-n|--new]}} -f {{494}} {{[-n|--new]}} -f {{523}}`
