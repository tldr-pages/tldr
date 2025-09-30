# pamfile

> Beschrijf Netpbm (PAM or PNM) bestanden.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- Beschrijf de gespecificeerde Netpbm bestanden:

`pamfile {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Beschrijf iedere afbeelding in ieder invoerbestand (in tegenstelling tot alleen de eerste afbeelding in elk bestand) in een machine-leesbaar formaat:

`pamfile {{[-a|-allimages]}} -machine {{pad/naar/bestand}}`

- Toon hoeveel afbeeldingen de invoerbestanden bevatten:

`pamfile {{[-cou|-count]}} {{pad/naar/bestand}}`
