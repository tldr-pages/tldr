# ned

> Like `grep` but with powerful replace capabilities.
> Unlike `sed`, as it isn't restricted to line oriented editing.
> More information: <https://github.com/nevdelap/ned#ned-usage>.

- Recursively search starting in the current directory, ignoring case:

`ned {{[-i|--ignore-case]}} {{[-R|--recursive]}} '{{^[dl]og}}' {{.}}`

- Search always showing colored output:

`ned --colors '{{^[dl]og}}' {{.}}`

- Search never showing colored output:

`ned --colors never '{{^[dl]og}}' {{.}}`

- Search ignoring certain files:

`ned {{[-R|--recursive]}} --exclude '{{*.htm}}' '{{^[dl]og}}' {{.}}`

- Simple replace:

`ned '{{dog}}' {{[-r|--replace]}} '{{cat}}' {{.}}`

- Replace using numbered group references:

`ned '{{the ([a-z]+) dog and the ([a-z]+) dog}}' {{[-r|--replace]}} '{{the $2 dog and the $1 dog}}' {{.}}`

- Replace changing case:

`ned '{{([a-z]+) dog}}' --case-replacements {{[-r|--replace]}} '{{\U$1\E! dog}}' --stdout {{.}}`

- Preview results of a find and replace without updating the target files:

`ned '{{^[sb]ad}}' {{[-r|--replace]}} '{{happy}}' --stdout {{.}}`
