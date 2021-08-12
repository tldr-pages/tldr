# tee

> Citiți de la intrarea standard și scrieți la ieșirea standard și fișiere (sau comenzi).
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/tee>

- Copiați intrarea standard în fiecare fișier și, de asemenea, la ieșirea standard:

`echo "example" | tee {{FILE}}`

- Adăugați la fișierele date, nu suprascrieți:

`echo "example" | tee -a {{FILE}}`

- Imprimați intrarea standard la terminal și, de asemenea, conduceți-l într-un alt program pentru prelucrare ulterioară:

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Creați un director numit „exemplu”, numărați numărul de caractere din „exemplu” și scrieți „exemplu” la terminal:

`echo "example" | tee >(xargs mkdir) >(wc -c)`
