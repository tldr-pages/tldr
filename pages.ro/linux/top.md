# top

> Afișează informații dinamice în timp real despre procesele care rulează.
> Mai multe informaţii: <https://manned.org/top>

- Start top:

`top`

- Nu afișa nici un proces inactiv sau zombie:

`top -i`

- Afișează numai procesele deținute de un anumit utilizator:

`top -u {{username}}`

- Sortarea proceselor după un câmp:

`top -o {{field_name}}`

- Afișați firele individuale ale unui anumit proces:

`top -Hp {{process_id}}`

- Afișați numai procesele cu PID-ul dat (e), trecut ca o listă separată prin virgulă. (În mod normal, nu ar ști PID-urile de pe mână. Acest exemplu alege PID-urile din numele procesului):

`top -p $(pgrep -d ',' {{process_name}})`

- Obțineți ajutor pentru comenzile interactive:

`?`
