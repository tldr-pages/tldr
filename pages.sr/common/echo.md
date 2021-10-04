# echo

> Prikazuje date argumente.
> Više informacija na: <https://www.gnu.org/software/coreutils/echo>.

- Prikazuje tekstualnu poruku. Napomena: navodnici su opcionalni:

`echo "{{Zdravo Svete}}"`

- Prikazuje poruku sa promenljivom:

`echo "{{Moja lokacija je $PATH}}"`

- Prikazuje poruku bez dodatne linije:

`echo -n "{{Zdravo Svete}}"`

- Dodaje poruku u fajl:

`echo "{{Zdravo Svete}}" >> {{fajl.txt}}`

- Omogućava interpretaciju posebnih karektera (prethodi im "\\"):

`echo -e "{{Kolona 1\tKolona 2}}"`
