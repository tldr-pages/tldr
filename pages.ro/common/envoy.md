# envoy

> Un manager de activități bazate pe PHP pentru serverele de la distanță Laravel.
> Mai multe informaţii: <https://laravel.com/docs/envoy>

- Iniţializarea unui fişier de configurare:

`envoy init {{host_name}}`

- Rulează o sarcină:

`envoy run {{task_name}}`

- Rulați o sarcină dintr-un anumit proiect:

`envoy run --path {{path/to/directory}} {{task_name}}`

- Rulați o sarcină și continuați eșecul:

`envoy run --continue {{task_name}}`

- Dump o sarcină ca un script bash pentru inspecție:

`envoy run --pretend {{task_name}}`

- Conectați-vă la serverul specificat prin SSH:

`envoy ssh {{server_name}}`
