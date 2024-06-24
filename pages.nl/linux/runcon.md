# runcon

> Voer een programma uit in een andere SELinux-beveiligingscontext.
> Bekijk ook: `secon`.
> Meer informatie: <https://www.gnu.org/software/coreutils/runcon>.

- Toon de beveiligingscontext van de huidige uitvoeringscontext:

`runcon`

- Specificeer het domein om een commando in uit te voeren:

`runcon -t {{domein}}_t {{commando}}`

- Specificeer de context rol om een commando mee uit te voeren:

`runcon -r {{rol}}_r {{commando}}`

- Specificeer de volledige context om een commando mee uit te voeren:

`runcon {{gebruiker}}_u:{{rol}}_r:{{domein}}_t {{commando}}`
