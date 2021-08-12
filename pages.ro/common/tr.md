# tr

> Traduceți caracterele: rulați înlocuiri bazate pe caractere unice și seturi de caractere.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/tr>

- Înlocuiți toate aparițiile unui caracter într-un fișier și imprimați rezultatul:

`tr {{find_character}} {{replace_character}} < {{filename}}`

- Înlocuiți toate aparițiile unui caracter din ieșirea altei comenzi:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- Harta fiecare caracter al primului set la caracterul corespunzător al celui de-al doilea set:

`tr '{{abcd}}' '{{jkmn}}' < {{filename}}`

- Ștergeți toate aparițiile setului specificat de caractere din intrare:

`tr -d '{{input_characters}}' < {{filename}}`

- Comprimați o serie de caractere identice cu un singur caracter:

`tr -s '{{input_characters}}' < {{filename}}`

- Traduceți conținutul unui fișier în majuscule:

`tr "[:lower:]" "[:upper:]" < {{filename}}`

- Scoateți caracterele care nu pot fi tipărite dintr-un fișier:

`tr -cd "[:print:]" < {{filename}}`
