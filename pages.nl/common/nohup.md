# nohup

> Laat een proces doorgaan wanneer de terminal wordt beëindigd.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>.

- Voer een proces uit dat kan doorgaan na het sluiten van de terminal:

`nohup {{commando}} {{argument1 argument2 ...}}`

- Start `nohup` in de achtergrondmodus:

`nohup {{commando}} {{argument1 argument2 ...}} &`

- Voer een shell-script uit dat kan doorgaan na het sluiten van de terminal:

`nohup {{pad/naar/script.sh}} &`

- Voer een proces uit en schrijf de uitvoer naar een specifiek bestand:

`nohup {{commando}} {{argument1 argument2 ...}} > {{pad/naar/uitvoer_bestand}} &`
