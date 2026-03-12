# sg run

> Run a one-time search or rewrite against a codebase using AST patterns.
> More information: <https://ast-grep.github.io/reference/cli/run.html>.

- Search for a pattern in the current directory:

`sg run --pattern '{{console.log($ARG)}}' --lang {{javascript}}`

- Replace a pattern with a new string across the codebase:

`sg run --pattern '{{var $NAME = $VALUE}}' --rewrite '{{let $NAME = $VALUE}}' --lang {{javascript}}`

- Search in specific directories or files:

`sg run --pattern '{{$PATTERN}}' --lang {{python}} {{path/to/directory1 path/to/directory2 ...}}`

- Interactively review and apply rewrites:

`sg run --pattern '{{useState<number>($A)}}' --rewrite '{{useState($A)}}' --lang {{typescript}} --interactive`

- Apply all rewrites without confirmation:

`sg run --pattern '{{old_function($ARGS)}}' --rewrite '{{new_function($ARGS)}}' --lang {{python}} --update-all`

- Output matches as JSON:

`sg run --pattern '{{$PATTERN}}' --lang {{rust}} --json`

- Show context lines around each match:

`sg run --pattern '{{$PATTERN}}' --lang {{go}} --context {{3}}`

- Print only file paths containing matches:

`sg run --pattern '{{$PATTERN}}' --lang {{java}} --files-with-matches`
