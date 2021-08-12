# shuf

> Generează permutări aleatorii.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/shuf>

- Randomizați ordinea liniilor dintr-un fișier și ieșiți rezultatul:

`shuf {{filename}}`

- Numai de ieșire primele 5 intrări ale rezultatului:

`shuf --head-count={{5}} {{filename}}`

- Scrieți ieșirea într-un alt fișier:

`shuf {{filename}} --output={{output_filename}}`

- Generați 3 numere aleatoare în intervalul 1-10 (inclusiv):

`shuf --head-count={{3}} --input-range={{1-10}} --repeat`
