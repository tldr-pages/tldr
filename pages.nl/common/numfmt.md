# numfmt

> Converteer getallen naar en van mens-leesbare strings.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>.

- Converteer 1.5K (SI-eenheden) naar 1500:

`numfmt --from si 1.5K`

- Converteer het 5e veld (1-gebaseerd) naar IEC-eenheden zonder de header te converteren:

`ls -l | numfmt --header=1 --field 5 --to iec`

- Converteer naar IEC-eenheden, opvullen met 5 tekens, links uitgelijnd:

`du {{[-s|--summarize]}} * | numfmt --to iec --format "%-5f"`
