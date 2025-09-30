# shred

> Overschrijf bestanden om gegevens veilig te verwijderen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html>.

- Overschrijf een bestand:

`shred {{pad/naar/bestand}}`

- Overschrijf een bestand en toon de voortgang op het scherm:

`shred {{[-v|--verbose]}} {{pad/naar/bestand}}`

- Overschrijf een bestand, waarbij nullen in plaats van willekeurige gegevens worden achtergelaten:

`shred {{[-z|--zero]}} {{pad/naar/bestand}}`

- Overschrijf een bestand een specifiek aantal keren:

`shred {{[-n|--iterations]}} {{25}} {{pad/naar/bestand}}`

- Overschrijf een bestand en verwijder het:

`shred {{[-u|--remove]}} {{pad/naar/bestand}}`

- Overschrijf een bestand 100 keer, voeg een laatste overschrijving met nullen toe, verwijder het bestand na overschrijven en toon verbose voortgang op het scherm:

`shred {{[-vzun|--verbose --zero --remove --iterations]}} 100 {{pad/naar/bestand}}`
