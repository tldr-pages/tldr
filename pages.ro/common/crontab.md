# crontab

> Programați lucrări cron pentru a rula pe un interval de timp pentru utilizatorul curent.
> Format de definiție a postului: „(min) (oră) (day_of_month) (lună) (day_of_week) command_to_execute”.
> Mai multe informaţii: <https://manned.org/crontab>

- Editează fișierul crontab pentru utilizatorul curent:

`crontab -e`

- Editați fișierul crontab pentru un anumit utilizator:

`sudo crontab -e -u {{user}}`

- Înlocuiți crontab-ul curent cu conținutul fișierului dat:

`crontab {{path/to/file}}`

- Vizualizați o listă de lucrări cron existente pentru utilizatorul curent:

`crontab -l`

- Eliminați toate lucrările cron pentru utilizatorul curent:

`crontab -r`

- Exemplu de locuri de muncă care rulează la 10:00 în fiecare zi (* înseamnă orice valoare):

`0 10 * * * {{command_to_execute}}`

- Exemplu de locuri de muncă care rulează în fiecare minut pe 3 aprilie:

`* * 3 Apr * {{command_to_execute}}`

- Exemplu de locuri de muncă care rulează un anumit script la 02:30 în fiecare vineri:

`30 2 * * Fri {{/absolute/path/to/script.sh}}`
