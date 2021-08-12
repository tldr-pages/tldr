# ffe

> Extrageți câmpuri dintr-un fișier de bază de date plat și scrieți în alt format.
> Un fișier de configurare este necesar pentru a interpreta intrarea și a formata ieșirea.
> Mai multe informaţii: <http://ff-extractor.sourceforge.net/ffe.html>

- Afișează toate datele de intrare utilizând configurația de date specificată:

`ffe --configuration={{path/to/config.ffe}} {{path/to/input}}`

- Conversia unui fișier de intrare într-un fișier de ieșire într-un format nou:

`ffe --output={{path/to/output}} -c {{path/to/config.ffe}} {{path/to/input}}`

- Selectați structura de intrare și formatul de imprimare din definițiile din fișierul de configurare `~/.fferc`:

`ffe --structure={{structure}} --print={{format}} {{path/to/input}}`

- Scrieți numai câmpurile selectate:

`ffe --field-list="{{FirstName,LastName,Age}}" -c {{path/to/config.ffe}} {{path/to/input}}`

- Scrieți numai înregistrările care se potrivesc cu o expresie:

`ffe -e "{{LastName=Smith}}" -c {{path/to/config.ffe}} {{path/to/input}}`

- Ajutor pentru afișare:

`ffe --help`
