# spfquery

> Interogare Expeditor politică cadru înregistrări pentru a valida expeditorii de poștă electronică.
> Mai multe informaţii: <https://www.libspf2.org/>

- Verificați dacă o adresă IP este permisă pentru a trimite un e-mail de la adresa de e-mail specificată:

`spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}}`

- Activați ieșirea de depanare:

`spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}} --debug`
