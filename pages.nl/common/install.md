# install

> Kopieer bestanden en stel attributen in.
> Kopieer bestanden (vaak uitvoerbare) naar een systeemlocatie zoals `/usr/local/bin` en geef ze de juiste permissies/eigendom.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

- Kopieer bestanden naar de bestemming:

`install {{pad/naar/bronbestand1 pad/naar/bronbestand2 ...}} {{pad/naar/bestemming}}`

- Kopieer bestanden naar de bestemming en stel hun eigendom in:

`install {{[-o|--owner]}} {{gebruiker}} {{pad/naar/bronbestand1 pad/naar/bronbestand2 ...}} {{pad/naar/bestemming}}`

- Kopieer bestanden naar de bestemming en stel hun groepseigendom in:

`install {{[-g|--group]}} {{gebruiker}} {{pad/naar/bronbestand1 pad/naar/bronbestand2 ...}} {{pad/naar/bestemming}}`

- Kopieer bestanden naar de bestemming en stel hun `modus` in:

`install {{[-m|--mode]}} {{+x}} {{pad/naar/bronbestand1 pad/naar/bronbestand2 ...}} {{pad/naar/bestemming}}`

- Kopieer bestanden en pas toegangstijden/wijzigingstijden van de bron toe op de bestemming:

`install {{[-p|--preserve-timestamps]}} {{pad/naar/bronbestand1 pad/naar/bronbestand2 ...}} {{pad/naar/bestemming}}`

- Kopieer bestanden en maak de mappen op de bestemming aan als ze niet bestaan:

`install -D {{pad/naar/bronbestand1 pad/naar/bronbestand2 ...}} {{pad/naar/bestemming}}`
