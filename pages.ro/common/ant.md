# ant

> Furnică apaşă.
> Instrument pentru construirea și gestionarea proiectelor bazate pe Java.
> Mai multe informaţii: <https://ant.apache.org>

- Construiți un proiect cu fișier de compilare implicit `build.xml`:

`ant`

- Construiți un proiect folosind un fișier de compilare altul decât `build.xml`:

`ant -f {{buildfile.xml}}`

- Imprimați informații cu privire la posibilele obiective pentru acest proiect:

`ant -p`

- Imprimare informații de depanare:

`ant -d`

- Executaţi toate ţintele care nu depind de ţintele eşuate:

`ant -k`
