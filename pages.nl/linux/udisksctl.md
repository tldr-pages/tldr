# udisksctl

> Communiceer met `udisksd` om opslagapparaten te bevragen en te manipuleren.
> Zie ook: `mount`.
> Meer informatie: <https://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- Toon algemene informatie over schijfstations en blokapparaten:

`udisksctl status`

- Toon gedetailleerde informatie over een apparaat:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdX}}`

- Toon gedetailleerde informatie over een apparaatpartitie:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdXN}}`

- Koppel een apparaatpartitie aan en toon het koppelpunt:

`udisksctl mount {{[-b|--block-device]}} {{/dev/sdXN}}`

- Ontkoppel een apparaatpartitie:

`udisksctl unmount {{[-b|--block-device]}} {{/dev/sdXN}}`

- Zet een apparaat uit om het veilig te verwijderen:

`udisksctl power-off {{[-b|--block-device]}} {{/dev/sdX}}`

- Monitor de daemon op gebeurtenissen:

`udisksctl monitor`
