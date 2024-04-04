# fgrep

> Zoek naar strings in bestanden.
> Gelijk aan `grep -F`.
> Meer informatie: <https://www.gnu.org/software/grep/manual/grep.html>.

- Zoek naar een string in een bestand:

`fgrep {{zoek_string}} {{pad/naar/bestand}}`

- Zoek in bestanden, maar alleen in regels die volledig overeenkomen:

`fgrep -x {{zoek_string}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Tel het aantal regels in een bestand die overeenkomen met de opgegeven string:

`fgrep -c {{zoek_string}} {{pad/naar/bestand}}`

- Toon de regelnummers in het bestand samen met de regel die overeenkomt:

`fgrep -n {{zoek_string}} {{pad/naar/bestand}}`

- Toon alle regels behalve de regels die de string bevatten:

`fgrep -v {{zoek_string}} {{pad/naar/bestand}}`

- Toon bestandsnamen waarvan de inhoud minimaal één keer overeenkomt met de string:

`fgrep -l {{zoek_string}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`
