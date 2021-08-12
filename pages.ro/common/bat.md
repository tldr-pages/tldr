# bat

> Imprimați și concatenați fișiere.
> O clonă `cat` cu evidențierea sintaxei și integrarea Git.
> Mai multe informaţii: <https://github.com/sharkdp/bat>

- Imprimați conținutul unui fișier la ieșirea standard:

`bat {{file}}`

- Concatenează mai multe fișiere în fișierul țintă:

`bat {{file1}} {{file2}} > {{target_file}}`

- Adăugați mai multe fișiere în fișierul țintă:

`bat {{file1}} {{file2}} >> {{target_file}}`

- Numarul tuturor liniilor de iesire:

`bat -n {{file}}`

- Sintaxa evidențiază un fișier json:

`bat --language json {{file.json}}`

- Afișează toate limbile acceptate:

`bat --list-languages`
