# mountpoint

> Testați dacă un director este un punct de montare al sistemului de fișiere.

- Verificați dacă un director este un punct de montare:

`mountpoint {{path/to/directory}}`

- Verificați dacă un director este un punct de montare fără a afișa nicio ieșire:

`mountpoint -q {{path/to/directory}}`

- Afișează numere majore/minore ale sistemului de fișiere al unui punct de montare:

`mountpoint --fs-devno {{path/to/directory}}`
