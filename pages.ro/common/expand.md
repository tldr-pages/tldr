# expand

> Conversia filelor în spații.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/expand>

- Convertiți filele din fiecare fișier în spații, scriind la ieșire standard:

`expand {{file}}`

- Conversia filelor în spații, citirea de la intrarea standard:

`expand`

- Nu convertiți filele după non spații:

`expand -i {{file}}`

- Au file un anumit număr de caractere în afară, nu 8:

`expand -t={{number}} {{file}}`

- Utilizați o listă separată prin virgulă a pozițiilor explicite ale filelor:

`expand -t={{1,4,6}}`
