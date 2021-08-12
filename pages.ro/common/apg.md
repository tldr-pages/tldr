# apg

> Creează parole aleatorii arbitrar complexe.
> Mai multe informaţii: <https://manned.org/apg>

- Creați parole aleatorii (lungimea implicită a parolei este 8):

`apg`

- Creați o parolă cu cel puțin 1 simbol (S), 1 număr (N), 1 majuscule (C), 1 minuscule (L):

`apg -M SNCL`

- Creați o parolă cu 16 caractere:

`apg -m {{16}}`

- Creați o parolă cu o lungime maximă de 16:

`apg -x {{16}}`

- Creați o parolă care nu apare într-un dicționar (fișierul dicționar trebuie furnizat):

`apg -r {{dictionary_file}}`
