# numfmt

> Converteer getallen naar en van voor mensen leesbare tekenreeksen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

- Converteer 1.5K (SI-eenheden) naar 1500:

`numfmt --from si 1.5K`

- Converteer 1500 naar 1.5K (SI-eenheden):

`numfmt --to si 1500`

- Converteer 1.5K (IEC-eenheden) naar 1536:

`numfmt --from iec 1.5K`

- Gebruik de juiste conversie op basis van het achtervoegsel:

`numfmt --from auto {{1.5Ki}}`

- Converteer het 5e veld (1-gebaseerd) naar IEC-eenheden zonder de koptekst te converteren:

`ls -l | numfmt --header=1 --field 5 --to iec`

- Converteer naar IEC-eenheden, vul aan met 5 tekens, links uitgelijnd:

`du {{[-s|--summarize]}} * | numfmt --to iec --format "%-5f"`
