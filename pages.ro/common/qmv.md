# qmv

> Mutați fișierele și directoarele utilizând editorul de text implicit pentru a defini numele fișierelor.
> Mai multe informaţii: <https://www.nongnu.org/renameutils/>

- Mutați un singur fișier (deschideți un editor cu numele fișierului sursă din stânga și numele fișierului țintă în dreapta):

`qmv {{source_file}}`

- Mutați mai multe fișiere JPG:

`qmv {{*.jpg}}`

- Mutați mai multe directoare:

`qmv -d {{path/to/directory1}} {{path/to/directory2}} {{path/to/directory3}}`

- Mutați toate fișierele și directoarele într-un director:

`qmv --recursive {{path/to/directory}}`

- Mutați fișierele, dar schimbați pozițiile sursei și numele fișierelor țintă în editor:

`qmv --option swap {{*.jpg}}`
