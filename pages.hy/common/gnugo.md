#gnugo

> Play Go հրամանի տողում:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/gnugo/gnugo_3.html>:.

- Սկսեք ինտերակտիվ Go խաղ.:

`gnugo`

- [Ինտերակտիվ] Խաղում մեկ անգամ քար դրեք 5-րդ շարքում և J սյունակում.:

`J5`

- Սկսեք խաղ 5 ֆորայով քարերով 5 մակարդակի հակառակորդի հետ.:

`gnugo --handicap 5 --level 5`

- Վերսկսեք խաղը կոնկրետ ֆայլից 123 քայլում:

`gnugo {{[-l|--infile]}} {{path/to/game.sgf}} {{[-L|--until]}} 123`

- Տվե՛ք պաշտոնի մոտավոր գնահատականը.:

`gnugo --score estimate {{[-l|--infile]}} {{path/to/game.sgf}}`
