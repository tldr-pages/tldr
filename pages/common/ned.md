# ned

> Is like grep, but with powerful replace capabilities, and unlike sed, as it isn't restricted to line oriented editing.

- Recursively search starting in the current directory, ignoring case:

`ned -iR '^[dl]og' .`

- Search always showing colored output:

`ned -c '^[dl]og' .`

- Search never showing colored output:

`ned --colors=never '^[dl]og' .`

- Set default arguments in your terminal environment:

`export NED_DEFAULTS='-i --colors=always'`

- Search ignoring certain files:

`ned -R --exclude '*.htm' '^[dl]og' .`

- Replace using numbered group references:

`ned 'the ([a-z]+) dog and the ([a-z]+) dog' -r 'the $2 dog and the $1 dog' .`

- Replace changing case:

`ned ' ([a-z]+) dog' --case-replacements -r '\U$1\E! dog' --stdout .`

- Replace and see the results in the terminal without updating the target files:

`ned '^[sb]ad' -r happy --stdout .`
