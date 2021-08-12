# psql

> Client de linie de comandă PostgreSQL.
> Mai multe informaţii: <https://www.postgresql.org/docs/current/app-psql.html>

Conectează-te la baza de date. Se conectează la localhost utilizând portul implicit 5432 cu utilizatorul implicit ca utilizator conectat în prezent:

`psql {{database}}`

- Conectează-te la baza de date pe un anumit server gazdă care rulează pe un anumit port cu un nume de utilizator dat, fără o solicitare de parolă:

`psql -h {{host}} -p {{port}} -U {{username}} {{database}}`

- Conectează-te la baza de date; utilizatorul va fi solicitat parola:

`psql -h {{host}} -p {{port}} -U {{username}} -W {{database}}`

- Executați o singură interogare SQL sau comanda PostgreSQL pe baza de date dată (utile în scripturi shell):

`psql -c '{{query}}' {{database}}`

- Execută comenzi dintr-un fișier din baza de date dată:

`psql {{database}} -f {{file.sql}}`
