# lastcomm

> A legutóbb végrehajtott parancsok megjelenítése. További információ: <https://manpages.debian.org/stable/acct/lastcomm.1.en.html>.

- Az acct-ben (rekordfájlban) lévő összes parancsra vonatkozó információk kinyomtatása:

`lastcomm`

- Egy adott felhasználó által végrehajtott parancsok megjelenítése:

`lastcomm --user {{user}}`

- Információk megjelenítése egy adott rendszerben végrehajtott parancsról:

`lastcomm --command {{command}}`

- Információk megjelenítése egy adott terminálon végrehajtott parancsokról:

`lastcomm --tty {{terminal_name}}`
