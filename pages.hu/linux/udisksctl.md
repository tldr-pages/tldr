# udisksctl

> Az udisksd daemon folyamattal való interakcióra használt parancssori program. További információ: <http://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- Magas szintű információk megjelenítése a lemezmeghajtókról és blokkeszközökről:

`udisksctl status`

- Részletes információk megjelenítése egy eszközről:

`udisksctl info --block-device {{/dev/sdX}}`

- Részletes információk megjelenítése egy eszközpartícióról:

`udisksctl info --block-device {{/dev/sdXN}}`

- Eszközpartíció csatolása és a csatolási pont kiírása:

`udisksctl mount --block-device {{/dev/sdXN}}`

- Egy eszközpartíció leválasztása:

`udisksctl unmount --block-device {{/dev/sdXN}}`

- A démon figyelése eseményekre:

`udisksctl monitor`
