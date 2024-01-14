# csplit

> Splits een bestand in stukken.
> Dit genereert bestanden zoals "xx00", "xx01" etc.
> Meer informatie: <https://www.gnu.org/software/coreutils/csplit>.

- Splits een bestand op regels 5 en 23:

`csplit {{pad/naar/bestand}} 5 23`

- Splits een bestand iedere 5 regels (dit zal falen als het totaal aantal regels niet deelbaar is door 5):

`csplit {{pad/naar/bestand}} 5 {*}`

- Splits een bestand iedere 5 regels en negeer de exacte verdeeldheid error:

`csplit -k {{pad/naar/bestand}} 5 {*}`

- Splits een bestand op regel 5 en gebruik een aangepaste prefix voor de uitvoerbestanden:

`csplit {{pad/naar/bestand}} 5 -f {{prefix}}`

- Splits een bestand op een regel die overeenkomt met de reguliere expressie:

`csplit {{pad/naar/bestand}} /{{reguliere_expressie}}/`
