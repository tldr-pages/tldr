# at

> Executați comenzi o dată la un moment ulterior.
> Service atd (sau atrun) ar trebui să fie difuzate pentru execuțiile reale.
> Mai multe informaţii: <https://man.archlinux.org/man/at.1>

- Executați comenzi de la intrarea standard în 5 minute (apăsați 'Ctrl + D 'când ați terminat):

`at now + 5 minutes`

- Execută o comandă de intrare standard la ora 10:00 astăzi:

`echo "{{./make_db_backup.sh}}" | at 1000`

- Execută comenzi dintr-un fișier dat marțea viitoare:

`at -f {{path/to/file}} 9:30 PM Tue`
