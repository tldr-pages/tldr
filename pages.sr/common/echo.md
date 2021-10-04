# echo

> Prikazuje date argumente.
> Više informacija na: <https://www.gnu.org/software/coreutils/echo>.

- Prikazuje tekstualnu poruku. Napomena: navodnici su opcionalni:

`echo "{{Hello World}}"`

- Prikazuje poruku sa promenljivom:

`echo "{{Moja lokacija je $PATH}}"`

- Prikazuje poruku bez dodatne linije:

`echo -n "{{Hello World}}"`

- Dodaje poruku u fajl:

`echo "{{Hello World}}" >> {{fajl.txt}}`

- Omogućava interpretaciju posebnih karektera (prethodi im "\\"):

`echo -e "{{Kolona 1\tKolona 2}}"`
