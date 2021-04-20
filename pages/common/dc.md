# dc

> An arbitrary precision calculator. Uses reverse polish notation (RPN).
> More information: <https://www.gnu.org/software/bc/manual/dc-1.05/html_mono/dc.html>.

- Run calculator in interactive mode:

`dc`

- Execute dc script in file:

`dc -f {{file}}`

- Calculate 4 times 5 [4 5 *], subtract 17 [17 -], and [p]rint the output (using echo):

`echo "4 5 * 17 - p"| dc`

- Set number of decimal places to 7 [7 k], calculate 5 divided by -3 [5 _3 /] and [p]rint (using dc -e):

`dc -e "7 k 5 _3 / p"`

- Calculate the golden ratio, phi: Set number of decimal places to 100 [100 k], square root of 5 [5 v] plus 1 [1 +], divided by 2 [2 /], and [p]rint result:

`dc -e "100 k 5 v 1 + 2 / p"`
