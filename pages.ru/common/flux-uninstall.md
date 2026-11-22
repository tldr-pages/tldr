# flux uninstall

> Удалять Flux и его пользовательские определения ресурсов.
> Больше информации: <https://fluxcd.io/flux/cmd/flux_uninstall/>.

- Удалить компоненты Flux, пользовательские ресурсы и пространство имён:

`flux uninstall`

- Удалить Flux без запроса подтверждения:

`flux uninstall {{[-s|--silent]}}`

- Удалить Flux из конкретного пространства имён:

`flux uninstall {{[-n|--namespace]}} {{пространство_имён}}`

- Удалить Flux, сохранив пространство имён:

`flux uninstall --keep-namespace`

- Сымитировать удаление Flux:

`flux uninstall --dry-run`
