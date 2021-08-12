# radare2

> Un set de instrumente de inginerie inversă.
> Mai multe informaţii: <https://radare.gitbooks.io/radare2book/>

- Deschideți un fișier în modul de scriere fără a analiza anteturile formatului de fișier:

`radare2 -nw {{path/to/binary}}`

- Depanarea unui program:

`radare2 -d {{path/to/binary}}`

- Rulați un script înainte de a intra în CLI interactiv:

`radare2 -i {{path/to/script.r2}} {{path/to/binary}}`

- Afișează textul de ajutor pentru orice comandă din CLI interactiv:

`> {{radare2_command}}?`

- Rulați o comandă shell de la CLI interactiv:

`> !{{shell_command}}`

- Dump octeți brute de bloc curent într-un fișier:

`> pr > {{path/to/file.bin}}`
