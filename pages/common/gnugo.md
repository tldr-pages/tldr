# gnugo

> Free program that plays Go on the command-line.
> More information: <https://www.gnu.org/software/gnugo>.

- Start an ASCII game of go:

`gnugo`

- Place a stone at row 5 and column J once in game:

`J5`

- Start a game with 5 handicap stones with opponent of level 5:

`gnugo --handicap 5 --level 5`

- Resume game at move 123:

`gnugo --infile game.sgf --until 123`

- Give a rough score estimate of a position:

`gnugo --score estimate --infile game.sgf`
