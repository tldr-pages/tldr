# dc

> Un calculator de precizie arbitrar. Utilizează notația poloneză inversă (RPN).
> Mai multe informaţii: <https://www.gnu.org/software/bc/manual/dc-1.05/html_mono/dc.html>

- Rulați calculatorul în modul interactiv:

`dc`

- Executați script dc în fișier:

`dc -f {{file}}`

- Se calculează de 4 ori 5 [4 5 *], scade 17 [17 -], și [p] rint ieșirea (folosind ecou):

`echo "4 5 * 17 - p"| dc`

- Setați numărul de zecimale la 7 [7 k], calculați 5 împărțit la -3 [5 _3/] și [p] rint (folosind dc -e):

`dc -e "7 k 5 _3 / p"`

- Se calculează raportul de aur, phi: Setați numărul de zecimale la 100 [100 k], rădăcină pătrată de 5 [5 v] plus 1 [1 +], împărțit la 2 [2/], și [p] rezultat rint:

`dc -e "100 k 5 v 1 + 2 / p"`
