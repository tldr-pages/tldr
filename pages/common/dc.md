# dc

> An arbitrary precision calculator. Uses reverse polish notation (RPN).

- Run calculator in interactive mode:

`dc`

- Calculate 4 times 5 [4 5 *], subtract 17 [17 -], and [p]rint the output :

`echo "4 5 * 17 - p"| dc`

- Set number of decimal places to 10 [k 7], calculate 5 divided by -3 [5 _3 /] and [p]rint:

`echo "7 k 5 _3 / p" | dc`

- To 100 decimal places [100 k], calculate the golden ratio, phi, sqrt(5) [5 v] plus 1 [1 +], divided by 2 [2 /], and [p]rint result:

`echo "100 k 5 v 1 + 2 / p" | dc`
