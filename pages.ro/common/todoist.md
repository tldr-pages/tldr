# todoist

> Acest program îți permite să folosești Todoist din linia de comandă.
> Mai multe informații: <https://github.com/sachaos/todoist>.

- Adaugă o sarcină:

`todoist add "{{o_sarcină}}"`

- Adaugă o sarcină cu prioritate ridicată cu o etichetă, proiect și dată scadentă:

`todoist add "{{o_sarcină}}" --priority {{1}} --label-ids "{{idul_etichetei}}" --project-name "{{numele_proiectului}}" --date "{{tmr 9am}}"`

- Adaugă o sarcină cu prioritate ridicată cu o etichetă, proiect și dată scadentă, folosind modul rapid:

`todoist quick '#{{numele_proiectului}} "{{tmr 9am}}" p{{1}} {{o_sarcină}} @{{numele_etichetei}}'`

- Enumeră toate sarcinile cu cap de tabel și culori:

`todoist --header --color list`

- Enumeră toate sarcinile cu prioritate ridicată:

`todoist list --filter p{{1}}`

- Enumeră toate sarcinile cu prioritate ridicată de astăzi care au eticheta specificată:

`todoist list --filter '(@{{numele_etichetei}} | {{today}}) & p{{1}}'`
