# roll

> Rolls a user-defined dice sequence.

- Roll 3 6-sided dice and sums the results:

`roll {{3}}{{d}}`

- Roll 1 8-sided die, add 3 and sum the results:

`roll {{d}}{{8}} + {{3}}`

- Roll 4 6-sided dice, keep the 3 highest results and sum the results:

`roll {{4}}{{d}}{{6}}{{h}}{{3}}`

- Roll 2 12-sided dice 2 times and show every roll:

`roll --verbose {{2}}{{{2}}{{d}}{{12}}}`

- Roll 2 20-sided dice until the result is bigger than 10:

`roll "{{2}}{{d}}{{20}}{{>}}{{10}}"`

- Roll 2 5-sided dice 3 times and show the total sum:

`roll --sum-series {{3}}{{{2}}{{d}}{{5}}}`
