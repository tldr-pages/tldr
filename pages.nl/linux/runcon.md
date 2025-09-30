# runcon

> Voer een programma uit in een andere SELinux-beveiligingscontext.
> Zie ook: `secon`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/runcon-invocation.html>.

- Toon de beveiligingscontext van de huidige uitvoeringscontext:

`runcon`

- Specificeer het domein om een commando in uit te voeren:

`runcon {{[-t|--type]}} {{domein}}_t {{commando}}`

- Specificeer de context rol om een commando mee uit te voeren:

`runcon {{[-r|--role]}} {{rol}}_r {{commando}}`

- Specificeer de volledige context om een commando mee uit te voeren:

`runcon {{gebruiker}}_u:{{rol}}_r:{{domein}}_t {{commando}}`
