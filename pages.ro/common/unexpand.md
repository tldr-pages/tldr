# unexpand

> Conversia spațiilor în file.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/unexpand>

- Convertiți spațiile libere din fiecare fișier în file, scriind la ieșirea standard:

`unexpand {{file}}`

- Conversia semifabricatelor în file, citirea de la ieșirea standard:

`unexpand`

- Convertiți toate semifabricatele, în loc de spații libere inițiale:

`unexpand -a {{file}}`

- Conversia doar secvențe de conducere de semifabricate (suprascrie -a):

`unexpand --first-only {{file}}`

- Au file un anumit număr de caractere în afară, nu 8 (permite -a):

`unexpand -t {{number}} {{file}}`
