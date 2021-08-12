# batch

> Executați comenzi la un moment ulterior, atunci când nivelurile de încărcare a sistemului permit.
> Service atd (sau atrun) ar trebui să fie difuzate pentru execuțiile reale.
> Mai multe informaţii: <https://man.archlinux.org/man/at.1>

- Executați comenzi de la intrarea standard (apăsați `Ctrl + D` când ați terminat):

`batch`

- Executa o comanda de la intrare standard:

`echo "{{./make_db_backup.sh}}" | batch`

- Executați comenzi dintr-un fișier dat:

`batch -f {{path/to/file}}`
