# audit2allow

> Scan logs voor berichten over geweigerde machtigingen.
> Genereer een rapport met Type Enforcement (TE) regels die succesvolle bewerkingen mogelijk toestaan.
> Zie ook: `audit2why`.
> Meer informatie: <https://manned.org/audit2allow>.

- Toon alle gegenereerde berichten in audit- en berichtlogs:

`audit2allow {{[-a|--all]}}`

- Toon alle gegenereerde berichten sinds de laatste keer opstarten:

`audit2allow {{[-b|--boot]}}`

- Toon gedetailleerde informatie rondom gegenereerde berichten:

`audit2allow {{[-e|--explain]}}`

- Schakel verbose output in:

`audit2allow {{[-v|--verbose]}}`

- Gebruik geïnstalleerde macro's om een referentiebeleid te genereren:

`audit2allow {{[-R|--reference]}}`

- Geef een beleidsbestand op voor verdere analyse:

`audit2allow {{[-p|--policy]}} {{pad/naar/beleidsbestand}}`

- Beperk de analyse tot berichten met een type dat is opgegeven in `regex`:

`audit2allow {{[-t|--type]}} {{type_regex}}`

- Toon de help:

`audit2allow {{[-h|--help]}}`
