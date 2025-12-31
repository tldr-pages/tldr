# audit2allow

> Genereer SELinux-beleidsregels op basis van auditlogs.
> Onderdeel van het `policycoreutils-python-utils` pakket.
> Zie ook: `audit2why`, `ausearch`, `semodule`.
> Meer informatie: <https://manned.org/audit2allow>.

- Genereer toestemmingsregels op basis van recente auditweigeringen en toon deze:

`sudo audit2allow {{[-a|--all]}}`

- Genereer toestemmingsregels op basis van een specifiek auditlogbestand:

`sudo audit2allow {{[-i|--input]}} {{pad/naar/audit.log}}`

- Genereer een beleidsmodule op basis van recente auditweigeringen:

`sudo audit2allow {{[-a|--all]}} {{[-M|--module]}} {{module_naam}}`

- Leg uit waarom SELinux-weigeringen plaatsvonden (hetzelfde als `audit2why`):

`sudo audit2allow {{[-a|--all]}} --why`

- Toon gedetailleerde informatie over gegenereerde berichten:

`sudo audit2allow {{[-a|--all]}} {{[-e|--explain]}}`

- Gebruik geïnstalleerde macro's om een referentiebeleid te genereren:

`sudo audit2allow {{[-a|--all]}} {{[-R|--reference]}}`

- Genereer toestemmingsregels voor een specifieke service:

`sudo ausearch {{[-m|--message]}} avc {{[-c|--comm]}} {{service_naam}} | audit2allow {{[-M|--module]}} {{beleidsnaam}}`

- Schakel uitgebreide uitvoermodus in:

`sudo audit2allow {{[-a|--all]}} {{[-v|--verbose]}}`
