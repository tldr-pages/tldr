# binwalk

> Instrument de analiză firmware.
> Mai multe informaţii: <https://github.com/ReFirmLabs/binwalk>

- Scanează un fișier binar:

`binwalk {{path/to/binary}}`

- Extrageți fișiere dintr-un binar, specificând directorul de ieșire:

`binwalk --extract --directory {{output_directory}} {{path/to/binary}}`

- Extragerea recursivă a fișierelor dintr-un binar care limitează adâncimea de recursie la 2:

`binwalk --extract --matryoshka --depth {{2}} {{path/to/binary}}`

- Extragerea fișierelor dintr-un binar cu semnătura fișierului specificată:

`binwalk --dd '{{png image:png}}' {{path/to/binary}}`

- Analizați entropia unui binar, salvând parcela cu același nume ca extensia binară și `.png` adăugată:

`binwalk --entropy --save {{path/to/binary}}`

- Combinați entropia, semnătura și analiza opcodurilor într-o singură comandă:

`binwalk --entropy --signature --opcodes {{path/to/binary}}`
