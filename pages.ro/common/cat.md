# cat

> Imprimați și concatenați fișiere.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/cat>

- Imprimați conținutul unui fișier la ieșirea standard:

`cat {{file}}`

- Concatenează mai multe fișiere în fișierul țintă:

`cat {{file1}} {{file2}} > {{target_file}}`

- Adăugați mai multe fișiere în fișierul țintă:

`cat {{file1}} {{file2}} >> {{target_file}}`

- Numarul tuturor liniilor de iesire:

`cat -n {{file}}`

- Afișarea caracterelor neimprimabile și spațiilor albe (cu prefixul „M” dacă nu este ASCII):

`cat -v -t -e {{file}}`
