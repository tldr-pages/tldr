# shred

> Overschrijf bestanden om gegevens veilig te verwijderen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html>.

- Overschrijf een bestand:

`shred {{pad/naar/bestand}}`

- Overschrijf een bestand en toon de voortgang op het scherm:

`shred --verbose {{pad/naar/bestand}}`

- Overschrijf een bestand, waarbij [z]ero's in plaats van willekeurige gegevens worden achtergelaten:

`shred --zero {{pad/naar/bestand}}`

- Overschrijf een bestand een specifiek aa[n]tal keren:

`shred --iterations {{25}} {{pad/naar/bestand}}`

- Overschrijf een bestand en verwijder het:

`shred --remove {{pad/naar/bestand}}`

- Overschrijf een bestand 100 keer, voeg een laatste overschrijving met [z]ero's toe, verwijder het bestand na overschrijven en toon [v]erbose voortgang op het scherm:

`shred -vzun 100 {{pad/naar/bestand}}`
