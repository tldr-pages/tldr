# pidstat

> Afișați utilizarea resurselor de sistem, inclusiv CPU, memorie, IO etc.

- Afișați statisticile procesorului la un interval de 2 secunde de 10 ori:

`pidstat {{2}} {{10}}`

- Afișează defecțiunile paginii și utilizarea memoriei:

`pidstat -r`

- Afișează utilizarea intrării/ieșirilor per ID proces:

`pidstat -d`

- Afișați informații despre un anumit PID:

`pidstat -p {{PID}}`

- Afișați statistici de memorie pentru toate procesele ale căror nume de comandă includ „vulpe” sau „pasăre”:

`pidstat -C "{{fox|bird}}" -r -p ALL`
