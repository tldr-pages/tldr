# gnugo

> Play Go on the command-line.
> More information: <https://www.gnu.org/software/gnugo/gnugo_3.html>.

- Start an interactive Go game:

`gnugo`

- [Interactive] Place a stone at row 5 and column J once in game:

`J5`

- Start a game with 5 handicap stones with opponent of level 5:

`gnugo --handicap 5 --level 5`

- Resume a game from a specific file at move 123:

`gnugo {{[-l|--infile]}} {{path/to/game.sgf}} {{[-L|--until]}} 123`

- Give a rough score estimate of a position:

`gnugo --score estimate {{[-l|--infile]}} game.sgf`
