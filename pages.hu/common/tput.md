# tput

> A terminál beállításainak és képességeinek megtekintése és módosítása. További információ: <https://manned.org/tput>.

- A kurzor mozgatása egy képernyőhelyre:

`tput cup {{row}} {{column}}`

- Az előtér (af) vagy a háttér (ab) színének beállítása:

`tput {{setaf|setab}} {{ansi_color_code}}`

- Az oszlopok, sorok vagy színek számának megjelenítése:

`tput {{cols|lines|colors}}`

- A terminál csengőjének megszólaltatása:

`tput bel`

- A terminál összes attribútumának visszaállítása:

`tput sgr0`

- A szóátlapolás engedélyezése vagy letiltása:

`tput {{smam|rmam}}`
