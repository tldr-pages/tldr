# diskutil

> Strumento per gestire i dischi locali e i volumi.
> Maggiori informazioni: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Mostra tutti i dischi correnti, le partizioni e i volumi montati:

`diskutil list`

- Ripara le strutture dati del filesystem di un volume:

`diskutil repairVolume {{/dev/diskX}}`

- Smonta un volume:

`diskutil unmountDisk {{/dev/diskX}}`

- Estrai un CD/DVD (smontando prima dell'estrazione):

`diskutil eject {{/dev/disk1}}`
