# noti

> Monitorizați un proces și declanșați o notificare banner.
> Mai multe informaţii: <https://github.com/variadico/noti>

- Afișează o notificare atunci când tar termină comprimarea fișierelor:

`noti {{tar -cjf example.tar.bz2 example/}}`

- Afișați o notificare chiar și atunci când o puneți după comanda pentru a viziona:

`{{command_to_watch}}; noti`

- Monitorizarea unui proces prin PID și declanșarea unei notificări atunci când PID dispare:

`noti -w {{process_id}}`
